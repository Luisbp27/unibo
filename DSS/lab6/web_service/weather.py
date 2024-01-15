# Import necessary libraries
from flask import Flask, render_template, request, jsonify
import requests

# OpenWeatherMap API base URL and your API key
BASE_URL = "http://api.weatherapi.com/v1/"
API_KEY = "cfe493cdd37e4489bc0185641231211"

# Initialize Flask app
app = Flask(__name__)

# Define a function to get weather data for a given location
def get_weather(city_name):
    # Make request to Weather.com API for current and forecast weather data
    onecall_response = requests.get(f"{BASE_URL}forecast.json?key={API_KEY}&q={city_name}&days=1&aqi=no&alerts=no")
    weather_data = onecall_response.json()

    # Extract relevant information from the API response
    current_conditions = weather_data["current"]
    hourly_forecast = weather_data["forecast"]["forecastday"][0]["hour"]
    daily_forecast = weather_data["forecast"]["forecastday"]

    # Return structured weather information
    return {
        "current_conditions": current_conditions,
        "hourly_forecast": hourly_forecast,
        "daily_forecast": daily_forecast
    }

# Define an endpoint for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['city_name']
        weather_info = get_weather(city_name)
        return render_template('index.html', city=city_name, weather_info=weather_info)
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
