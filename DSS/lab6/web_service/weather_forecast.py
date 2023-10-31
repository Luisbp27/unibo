# Import necessary libraries
from flask import Flask, request, jsonify
import requests

# Initialize Flask application
app = Flask(__name__)

# OpenWeatherMap API base URL and your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/"
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

# Define API endpoint for weather forecast
@app.route('/weather', methods=['GET'])
def get_weather():
    # Get parameters from the request
    location = request.args.get('location')
    timeframe = request.args.get('timeframe')  # 'hourly' or 'daily'

    # Make request to OpenWeatherMap API for current weather data
    current_weather_response = requests.get(f"{BASE_URL}weather?q={location}&appid={API_KEY}")
    current_weather_data = current_weather_response.json()

    # Initialize forecast data variables
    hourly_forecast_data = []
    daily_forecast_data = []

    # Handle different timeframes (hourly or daily)
    if timeframe == 'hourly':
        # Make request to OpenWeatherMap API for hourly forecast data
        hourly_forecast_response = requests.get(f"{BASE_URL}forecast?q={location}&appid={API_KEY}")
        hourly_forecast_data = hourly_forecast_response.json()['list']
        
        # Parse and structure the hourly forecast data as needed
        for forecast in hourly_forecast_data:
            forecast['temperature'] = forecast['main']['temp']
            forecast['description'] = forecast['weather'][0]['description']
            forecast['timestamp'] = forecast['dt']
            del forecast['main']
            del forecast['weather']
            del forecast['dt']


    elif timeframe == 'daily':
        # Make request to OpenWeatherMap API for daily forecast data
        daily_forecast_response = requests.get(f"{BASE_URL}forecast/daily?q={location}&cnt=7&appid={API_KEY}")
        daily_forecast_data = daily_forecast_response.json()['list']

        # Parse and structure the daily forecast data as needed
        for forecast in daily_forecast_data:
            forecast['temperature'] = forecast['temp']['day']
            forecast['description'] = forecast['weather'][0]['description']
            forecast['timestamp'] = forecast['dt']
            del forecast['temp']
            del forecast['weather']
            del forecast['dt']

    else:
        return jsonify({"error": "Invalid timeframe parameter"}), 400

    # Structure the response data
    weather_response = {
        "current_conditions": {
            "temperature": current_weather_data['main']['temp'],
            "description": current_weather_data['weather'][0]['description']
        },
        "hourly_forecast": hourly_forecast_data,
        "daily_forecast": daily_forecast_data
    }

    return jsonify(weather_response)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
