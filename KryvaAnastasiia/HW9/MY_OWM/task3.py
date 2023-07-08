
from pyowm import OWM
import config
import tkinter as tk
from tkinter import font

HEIGHT = 350
WIDTH = 450

def weather_response():
    user_city = entry_field.get()
    owm = OWM(config.KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(user_city)
    w = observation.weather
    w.detailed_status       # 'clouds'
    speed_wind = w.wind()
    speed_wind['speed']                 # {'speed': 4.6, 'deg': 330}
    w.humidity            # 87
    w.temperature('celsius') # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                 # {}
# print(w.heat_index)            # None
    w.clouds              # 75
    return f"City: {user_city} \nConditions : {w.detailed_status} \nTemperature is {round(w.temperature('celsius')['temp'], 2)} C \nWind speed is {w.wind()['speed']} km\hours \nHumidity of the air is {w.humidity}\nCloud coverage is {w.clouds}%"

def get_weather():
    label['text'] = weather_response()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()