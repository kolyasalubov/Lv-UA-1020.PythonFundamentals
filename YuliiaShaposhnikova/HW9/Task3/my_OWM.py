from pyowm import OWM
import config



owm = OWM(config.API_KEY)
mgr = owm.weather_manager()


def get_weather(city):

    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')
    wind_speed = w.wind()


    return f"Temperature: {temp['temp']} °C\nClouds: {w.detailed_status}\nHumidity: {w.humidity}\n" \
           f"Wind: {wind_speed['speed']}\nClouds: {w.clouds}"


