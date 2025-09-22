import requests
import json

# WeatherAPI key
WEATHER_API_KEY = '962f4a78d4454380829211314252209'  # TODO: Replace with your own WeatherAPI key
ENDPOINT = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    url = f"{ENDPOINT}?key={WEATHER_API_KEY}&q={city}"

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(url)
    # print(f"Response: {response}")

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        data = response.json()
        # print(f"Data: {data}")

        # Extract specific weather data
        temperature = data['current']['temp_f']  
        feelsLike = data['current']['feelslike_f']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']  
        windSpeed = data['current']['wind_mph']
        direction = data['current']['wind_dir']
        pressure = data['current']['pressure_mb']
        uv = data['current']['uv']
        cloud = data['current']['cloud']        
        visibility = data['current']['vis_miles']

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather in {city}")
        print(f"Temperature: {temperature} degrees Farenheit. (Feels like: {feelsLike} degrees Farenheit)")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {windSpeed} mph, Direction: {direction}")
        print(f"Pressure: {pressure} mb")
        print(f"UV Index: {uv}")
        print(f"Cloud Cover: {cloud}%")
        print(f"Visibility {visibility} miles")

    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if (response.status_code == 400): 
            print(f"Error: {response.status_code}. Bad request")
        elif (response.status_code == 401): 
            print(f"Error: {response.status_code}. Unauthorized access")
        elif (response.status_code == 404): 
            print(f"Error: {response.status_code}. Not found")
        else: 
            print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input('Enter a city name: ')
    
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
