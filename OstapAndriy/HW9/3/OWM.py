from pyowm import OWM
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
    weather_info = weather_info + "Хмарність: " + str(w.detailed_status) + "\n"
    weather_info = weather_info + "Швидкість вітру: " + str(speed_wind["speed"]) + "\n"
    weather_info = weather_info + "Вологість повітря: " + str(w.humidity) + "\n"
    weather_info = weather_info + "Поточна температура: " + str(massege["temp"]) + "\n"
    weather_info = weather_info + "Максимальна температура: " + str(massege["temp_max"]) + "\n"
    weather_info = weather_info + "Мінімальна температура: " + str(massege["temp_min"]) + "\n"
    weather_info = weather_info + "Температура на відчуття: " + str(massege["feels_like"]) + "\n"
    return weather_info