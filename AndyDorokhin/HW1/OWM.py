##############################
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

try:
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    input_city = input("In which city are you interested in the weather?:")

    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(input_city)
    w = observation.weather

    # w.detailed_status         # 'clouds'
    # w.wind()                  # {'speed': 4.6, 'deg': 330}
    # w.humidity                # 87
    # w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # w.rain                    # {}
    # w.heat_index              # None
    # w.clouds                  # 75

    print(f"City: {input_city}\nConditions: {w.detailed_status }\nTemperature is {round(w.temperature('celsius')['temp'], 2)} C")

    print(f"Wind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}" )

except:
    print('''Oops! There was a problem\nretrieving that information.''')
