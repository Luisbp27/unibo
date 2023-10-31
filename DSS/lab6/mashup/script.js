async function getWeatherData() {
    const location = document.getElementById('location').value;

    // Fetch data from Weather.com API
    const weatherComResponse = await fetch(`https://api.weather.com/data/2.5/weather?q=${location}&units=metric&appid=YOUR_WEATHERCOM_API_KEY`);
    const weatherComData = await weatherComResponse.json();

    // Fetch data from OpenWeatherMap API
    const openWeatherResponse = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${location}&units=metric&appid=YOUR_OPENWEATHERMAP_API_KEY`);
    const openWeatherData = await openWeatherResponse.json();

    // Process and display data
    displayWeatherData(weatherComData, openWeatherData);
}

function displayWeatherData(weatherComData, openWeatherData) {
    // Process and display data in the .weather-results div
    // Example: Display current temperature from Weather.com and OpenWeatherMap
    const weatherResultsDiv = document.querySelector('.weather-results');
    weatherResultsDiv.innerHTML = `
        <h2>Weather Forecast for ${weatherComData.name}</h2>
        <p>Temperature (Weather.com): ${weatherComData.main.temp}°C</p>
        <p>Temperature (OpenWeatherMap): ${openWeatherData.main.temp}°C</p>
        <!-- Add more weather information here -->
    `;
}
