Weather and Time Information Display
This Python application provides a transparent window that displays the current time, date, and weather information. It updates the weather every 10 minutes and the time every second. The weather icons change based on the current weather conditions.

Features
Transparent window that displays time, date, and weather information.
Automatic update of time every second.
Automatic update of weather information every 10 minutes.
Customizable weather icons based on current weather conditions (day/night, rain, snow, etc.).
Requirements
Python 3.7+
tkinter for GUI
Pillow for image handling
requests for API requests
Installation
Clone the repository:

git clone https://github.com/yourusername/weather-time-display.git
cd weather-time-display

Install the required packages:

pip install requests Pillow

Place the weather icons in the same directory as the script:

rain_snow.webp
rainy.webp
snowy.webp
cloudy.webp
sunny.webp
night.webp
Usage
Run the script

How it works
Fetching IP and Location Data:
The script first retrieves the user's IP address and location data using the get_ip function. This data is used to get the latitude, longitude, and timezone.

Fetching Weather Data:
Using the latitude, longitude, and timezone, the script fetches the current weather information from the Open-Meteo API via the get_weather function.

Fetching Time Data:
The current time is fetched using the World Time API with the get_time function.

Displaying Information:
The script then displays the time, date, and weather information in a transparent tkinter window. It updates the time every second with the update_time function and the weather information every 10 minutes with the update_weather function.

Configuration
Font Customization:
The font family and size for the displayed text can be changed in the script:

big_font = font.Font(family="Dancing Script", size=50)
small_font = font.Font(family="Dancing Script", size=25)

Weather Icons:
Ensure that the appropriate weather icon files (.webp format) are available in the same directory as the script. The icons are chosen based on the weather conditions.

Error Handling
The script includes error handling for API requests. If an error occurs during data fetching, it prints an error message and skips the update.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Weather data provided by Open-Meteo (https://open-meteo.com/).
Time data provided by World Time API (http://worldtimeapi.org/).
Location data provided by IP-API (http://ip-api.com/).
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

