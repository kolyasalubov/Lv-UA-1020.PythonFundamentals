from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps
import config

# ---------- FREE API KEY examples ---------------------

owm = OWM(config.KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details


def get_weather(city):
    weather_info = ''
    observation = mgr.weather_at_place(city)
    w = observation.weather
    speed_wind = w.wind()
    massege = w.temperature('celsius')
    weather_info = weather_info + "Cloudiness: " + str(w.detailed_status) + "\n"
    weather_info = weather_info + "Wind speed: " + str(speed_wind["speed"]) + "\n"
    weather_info = weather_info + "Air humidity: " + str(w.humidity) + "\n"
    weather_info = weather_info + "Сurrent temperature: " + str(massege["temp"]) + "\n"
    weather_info = weather_info + "Maximum temperature: " + str(massege["temp_max"]) + "\n"
    weather_info = weather_info + "Minimum temperature: " + str(massege["temp_min"]) + "\n"
    weather_info = weather_info + "Temperature feels like: " + str(massege["feels_like"]) + "\n"
    return weather_info

# w.rain                                           # {}
# w.heat_index                                     # None
# w.clouds                                         # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
# forecast = mgr.forecast_at_place('Milan,IT', 'daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())