from pyowm import OWM
import config


API_KEY = config.KEY
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
def weather_data(place_forecast: str) ->object:
    observation = mgr.weather_at_place(place_forecast) #('London,GB')
    return observation.weather

# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75





