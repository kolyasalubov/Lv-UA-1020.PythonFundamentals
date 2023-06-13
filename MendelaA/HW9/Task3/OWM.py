from pyowm import OWM
import config


def get_weather(city_name):
    
    owm = OWM(config.KEY)
    mgr = owm.weather_manager()
    
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city_name)
    w = observation.weather

    # print(w.detailed_status)         # 'clouds'
    # print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    # print(w.humidity)                # 87
    # print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    # print(w.rain)                    # {}
    # print(w.heat_index)              # None
    # print(w.clouds)                  # 75

    return (f'{w.detailed_status}\n'
            f'{w.wind()}\n'
            f'{w.humidity}\n'
            f'{w.temperature("celsius")}\n'
            f'{w.rain}\n'
            f'{w.heat_index}\n'
            f'{w.clouds}'
            ) 

