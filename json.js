const api_key = "63a90ae96d390ec37d6c1252f5a86e1a";
const base_url = "http://api.openweathermap.org/data/2.5/weather?";

const input = document.getElementById("input");
const button = document.getElementById("button");
const output = document.getElementById("output");

button.addEventListener("click", function() {
  const city_name = input.value;
  const complete_url = base_url + "appid=" + api_key + "&q=" + city_name;

  fetch(complete_url)
    .then(function(response) {
      return response.json();
    })

    .then(function(data) {
      if (data.cod != "404") {
        const temp = data.main.temp;
        const pressure = data.main.pressure;
        const humidity = data.main.humidity;
        const weather_description = data.weather[0].description;

        const output_text =
          `Temperature: ${temp} Kelvin<br>` +
          `Pressure: ${pressure} hPa<br>` +
          `Humidity: ${humidity} %<br>` +
          `Weather: ${weather_description}`;
        output.innerHTML = output_text;

      } else {
        output.innerHTML = "City not found. Please enter a valid city name.";
      }
    })

    .catch(function(error) {
      output.innerHTML = "Something went wrong. Please try again later.";
    });
});