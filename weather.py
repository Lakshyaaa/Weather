import tkinter as tk
from tkinter import messagebox
import requests
from requests.exceptions import RequestException

# Function to get current and forecast weather data
def get_weather(city):
    api_key = "Replace with your valid OpenWeatherMap API key"  
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    try:
        # Get current weather
        current_response = requests.get(current_weather_url, timeout=10)
        current_data = current_response.json()
        print(current_data)  # Debug: Print current weather response
        
        if current_data['cod'] != 200:
            return "City not found!"

        # Extract current weather information
        weather_desc = current_data['weather'][0]['description'].capitalize()
        temperature = current_data['main']['temp']
        humidity = current_data['main']['humidity']
        
        current_weather_info = f"Current Weather:\nWeather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\n"

        # Get forecast weather
        forecast_response = requests.get(forecast_url, timeout=10)
        forecast_data = forecast_response.json()
        print(forecast_data)  # Debug: Print forecast response

        if forecast_data['cod'] != "200":
            return "City not found!"

        # Extract forecast for the next 24 hours (first entry in forecast list)
        forecast_list = forecast_data['list'][:5]  # Get next few intervals (3-hour intervals)
        forecast_info = "Forecast (Next 24 hours):\n"
        for forecast in forecast_list:
            time = forecast['dt_txt']
            forecast_desc = forecast['weather'][0]['description'].capitalize()
            temp = forecast['main']['temp']
            forecast_info += f"{time}: {forecast_desc}, {temp}°C\n"

        # Combine current and forecast info
        full_info = current_weather_info + "\n" + forecast_info
        return full_info
    
    except RequestException as e:
        return f"Error: {str(e)}"

# Function to display weather info
def display_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        result_label.config(text=weather_info)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the label, entry, and button
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.geometry("400x400")
root.mainloop()
