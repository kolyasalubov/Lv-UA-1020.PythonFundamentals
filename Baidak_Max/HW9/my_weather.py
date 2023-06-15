from pyowm import OWM
from config import API_KEY



# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('cape town')
# w = observation.weather
#
# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75
def weather_user():
    city = input("Enter a city in which you want to look a weather? ")
    observation = mgr.weather_at_place(city)
    w = observation.weather
    rain = "Can be a rainy today" if w.rain else "No rain today"

    return(f"Temperature is: {w.temperature('celsius')['temp']} "
          f"\nFeels like: {w.temperature('celsius')['feels_like']} "
          f"\n{w.detailed_status.capitalize()}"
          f"\nWind speed {w.wind()['speed']}"
          f"\n{rain}")

print(weather_user())