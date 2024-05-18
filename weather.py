import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests
import os
from urllib.parse import quote

def get_weather(location_lon, location_lat, api_timezone):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={location_lon}&longitude={location_lat}&current=temperature_2m,apparent_temperature,is_day,rain,showers,snowfall&timezone={api_timezone}"
        print (url)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_ip():
    try:
        url = "http://ip-api.com/json/?fields=61439"
        response = requests.get(url)
        response.raise_for_status()
        ip_data = response.json()
        return ip_data
    except requests.RequestException as e:
        print(f"Error fetching time data: {e}")
        return None
    
def get_time():
    try:
        url = "http://worldtimeapi.org/api/ip"
        response = requests.get(url)
        response.raise_for_status()
        time_data = response.json()
        return time_data
    except requests.RequestException as e:
        print(f"Error fetching time data: {e}")
        return None

def update_time():
    time_data = get_time()
    if time_data:
        current_time = time_data['datetime'][11:19]  # Get hours, minutes, and seconds
        date = time_data['datetime'][:10]
        time_label.config(text=current_time)
        date_label.config(text=date)
    root.after(1000, update_time)  # Update time every second

def display_info():
    ip_data = get_ip()
    if ip_data:
        location_lat = ip_data['lat']
        location_lon = ip_data['lon']
        print (ip_data)
        timezone = ip_data['timezone']
        api_timezone = quote(timezone)
        weather = get_weather(location_lat, location_lon, api_timezone)
        time_data = get_time()
        ip_data = get_ip()


    if weather and time_data:
        global root, time_label, date_label
        
        root = tk.Tk()
        root.title("Weather and Time Information")

        # Make the window transparent
        root.overrideredirect(True)
        root.attributes("-transparentcolor", root["bg"])

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the position for placing the window in the top-left quarter
        window_width = 600
        window_height = 200
        x = screen_width // 2 - window_width // 2
        y = screen_height // 8 - window_height // 2

        # Set the window position
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Fancy font
        big_font = font.Font(family="Dancing Script", size=50)  # Using a fancy font
        small_font = font.Font(family="Dancing Script", size=25)

        # Create a transparent canvas
        canvas = tk.Canvas(root, width=window_width, height=window_height, bd=0, highlightthickness=0, bg=root["bg"])
        canvas.pack()

        # Time label with transparent background
        time_label = tk.Label(canvas, text="", font=big_font, bg=root["bg"], fg="white")
        time_label.pack(side=tk.TOP, padx=20, pady=10)

        # Load the weather icon
        weather_icon_path = os.path.join(os.path.dirname(__file__), "weather.webp")
        try:
            weather_icon = Image.open(weather_icon_path)
        except FileNotFoundError:
            print(f"Weather icon file not found at: {weather_icon_path}")
            return
        except Image.UnidentifiedImageError:
            print(f"Unidentified image error for file: {weather_icon_path}")
            return

        weather_icon = weather_icon.resize((75, 75), Image.LANCZOS)
        weather_icon = ImageTk.PhotoImage(weather_icon)
        
        icon_label = tk.Label(canvas, image=weather_icon, bg=root["bg"])
        icon_label.image = weather_icon  # keep a reference!
        icon_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Temperature label with transparent background
        temperature_label = tk.Label(canvas, text=f"{weather['current']['temperature_2m']}°C", font=small_font, bg=root["bg"], fg="white")
        temperature_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Date label with transparent background
        date_label = tk.Label(canvas, text="", font=small_font, bg=root["bg"], fg="white")
        date_label.pack(side=tk.TOP, padx=10, pady=10)

        update_time()  # Initialize time update

        root.mainloop()

    else:
        print("Error fetching data")

if __name__ == "__main__":
    display_info()
