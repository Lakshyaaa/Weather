**# Weather Prediction Application using Python and Tkinter**

This Python application provides both the current weather conditions and future weather forecast for a city entered by the user. It uses the Tkinter library for building the graphical user interface (GUI) and the OpenWeatherMap API to retrieve weather data. The app fetches and displays the current temperature, humidity, and weather description, along with the forecast for the next 24 hours.

**Key Features:**

User Input: The user can enter a city name in the text field provided in the GUI.

Current Weather: After the user submits the city name, the application will display the current weather conditions, including:

    Weather description (e.g., "Clear sky", "Rain")

    Temperature (in Celsius)

    Humidity (percentage)

Future Weather Forecast: The application also provides a weather forecast for the next 24 hours, broken down into 3-hour intervals. For each interval, it displays:

    Forecasted weather description

    Forecasted temperature

**How It Works:**

User Interaction: The user enters a city name in the input box and clicks the "Get Weather" button.

Weather Data Retrieval: The app sends two requests to the OpenWeatherMap API:

    Current Weather API: To fetch the current weather information.

    5-Day/3-Hour Forecast API: To fetch weather predictions for the upcoming 24 hours.

Data Display: The fetched weather data is displayed in the GUI. It shows the current weather followed by the forecast for the next few time intervals (3-hourly forecasts).

Error Handling: If the user enters an invalid city name or if there is an issue with the API request, the app will notify the user that the city was not found.

**Technologies Used:**

Python: Main programming language.

Tkinter: For building the GUI.

Requests: For making API calls to OpenWeatherMap.

OpenWeatherMap API: Provides weather data (both current and forecast).

**API Requests:**

Current Weather:

    Fetches the current temperature, weather description, and humidity for the given city.

Forecast Weather:

    Fetches the forecast for the next 24 hours, showing weather in 3-hour intervals.  
