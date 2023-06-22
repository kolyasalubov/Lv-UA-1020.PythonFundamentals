from pyowm import OWM
import config


def get_weather(city_name:str)->str:
    """
    Get weather from api
    """    
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

    return (f'Humidity is {w.humidity} %\n'
            f'Wind speed is {w.wind()["speed"]} km/hours\n'
            f'Temperature is {w.temperature("celsius")["temp"]} C\n'
            #f'{w.rain}\n'
            #'Heat index is {w.heat_index}\n'
            f'Clouds is {w.clouds} %'
            ) 

if __name__ == '__main__':
    print(get_weather('Lviv'))