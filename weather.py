import requests

# Class initialize
class Weather:
    # takes in api key and adds the base link in order to call the api
    def __init__(self, apiKey="cddb5cb0fb34ccfeeb382d50becf9dee"):
        self.apiKey = apiKey
        self.baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    # calls api to pull weather information. ensures a successful call to the api.
    def getWeatherData(self, cityName):
        url = f"{self.baseUrl}?q={cityName}&appid={self.apiKey}&units=imperial"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to fetch weather data.")
            return None

    # Allows the weather to be parsed into proper format if viewed in terminal
    def _parse_weather_data(self, data):
        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "city": data["name"],
            "country": data["sys"]["country"],
        }
        return weather

    # allows to view the information on terminal in a user friendly interface
    def display_weather(self, weather_data):
        return f"Weather in {weather_data['city']}, {weather_data['country']}:\n Temperature: {weather_data['temperature']}°F\n Humidity: {weather_data['humidity']}%\n Condition: {weather_data['condition']}\n Description: {weather_data['description']}\n Wind Speed: {weather_data['wind_speed']} m/s\n"


# Testing the api call information in terminal
def main():
    weather = Weather()
    city = str(input("Enter a city: "))
    weather_data = weather.getWeatherData(city)
    parse_data = weather._parse_weather_data(weather_data)
    print(weather.display_weather(parse_data))


if __name__ == "__main__":
    weather = Weather()

