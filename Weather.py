import requests

api_key = "63a90ae96d390ec37d6c1252f5a86e1a"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

data = response.json()

if data["cod"] != "404":

    main_data = data["main"]
    temp = main_data["temp"]
    pressure = main_data["pressure"]
    humidity = main_data["humidity"]
    weather_data = data["weather"]
    weather_description = weather_data[0]["description"]

    celcius =int(temp-273.15)


    print(f"Temperature: {temp} Kelvin ({celcius} Celcius)")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity} %")
    print(f"Weather: {weather_description}")

else:
    print("City not found. Please enter a valid city name.")
