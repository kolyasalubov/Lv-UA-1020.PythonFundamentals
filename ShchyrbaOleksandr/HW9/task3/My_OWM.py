from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
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
    weather_info = weather_info + "Current temperature: " + str(massege["temp"]) + "\n"
    weather_info = weather_info + "Maximum temperature: " + str(massege["temp_max"]) + "\n"
    weather_info = weather_info + "Minimum temperature: " + str(massege["temp_min"]) + "\n"
    weather_info = weather_info + "Temperature feels like: " + str(massege["feels_like"]) + "\n"
    return weather_info          
