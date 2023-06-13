from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def weather(location):

    # get weather data from OWM
    observation = mgr.weather_at_place(location)
    w = observation.weather

    # 'translate' wind direction to human-friendle representation
    directions = ('North', 'Nord-East', 'East', 'South-East',
                  'South', 'South-West', 'West', 'North-West')
    wind_deg = w.wind()['deg']
    marker = 23
    for i in range(0, 9):
        if wind_deg < marker + 45 * i:
            wind_direction = directions[i]
            break

    # get dict of temperatures
    temperat = w.temperature("celsius")

    # return string to be printed in GUI's lower frame
    return f'Description: {w.detailed_status}\n\nWind:\n    speed: {w.wind()["speed"]} m/s\n    direction: {wind_direction}\n\nHumidity: {w.humidity}%\n\nTemperature (Celcius):\n    current: {temperat["temp"]}\n    feels like: {temperat["feels_like"]}\n    maximum: {temperat["temp_max"]}\n    minimum: {temperat["temp_min"]}'
