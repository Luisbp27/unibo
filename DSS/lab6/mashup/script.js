const apiKey1 = '0a03a25cf192bc3eaa74a7784b0b69c9'; // Replace with your API key
const apiKey2 = 'cfe493cdd37e4489bc0185641231211'; // Replace with your API key

async function getWeather() {
    const location = document.getElementById('location').value;
    const url1 = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey1}`;
    const url2 = `http://api.weatherapi.com/v1/current.json?key=${apiKey2}&q=${location}&aqi=no`;

    try {
        const [data1, data2] = await Promise.all([
            fetch(url1).then(response => response.json()),
            fetch(url2).then(response => response.json())
        ]);

        // Process and display the weather data
        displayWeather(data1, data2);
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

// script.js
function displayWeather(data1, data2) {
    const weatherInfo = document.getElementById('weather-info');

    const location = `${data1.name}, ${data1.sys.country}`;
    const tempOWM = `${(data1.main.temp - 273.15).toFixed(2)}°C`; // Convert temperature from Kelvin to Celsius
    const tempWeatherAPI = `${data2.current.temp_c}°C`;

    const descriptionOWM = data1.weather[0].description;
    const descriptionWeatherAPI = data2.current.condition.text;

    const html = `
        <h2>${location}</h2>
        <div class="weather-details">
            <div>
                <p><strong>Current Temperature (OpenWeatherMap):</strong> ${tempOWM}</p>
                <p><strong>Description (OpenWeatherMap):</strong> ${descriptionOWM}</p>
            </div>
            <div>
                <p><strong>Current Temperature (WeatherAPI):</strong> ${tempWeatherAPI}</p>
                <p><strong>Description (WeatherAPI):</strong> ${descriptionWeatherAPI}</p>
            </div>
        </div>
    `;

    weatherInfo.innerHTML = html;
}

