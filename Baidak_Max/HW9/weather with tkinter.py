import tkinter as tk
from tkinter import font
from pyowm import OWM
from config import API_KEY


# API_KEY = '7ad49812045a6df69f139801e986c20b'
# created a config folder and put the key in it, commented out the key to check that it works


owm = OWM(API_KEY)
mgr = owm.weather_manager()


def weather_today():
    city_user = entry_field.get()
    observation = mgr.weather_at_place(city_user)
    w = observation.weather
    rain = "Can be a rainy today" if w.rain else "No rain today"

    label.config(text=f"Temperature is: {w.temperature('celsius')['temp']} "
          f"\nFeels like: {w.temperature('celsius')['feels_like']} "
          f"\n{w.detailed_status.capitalize()}"
          f"\nWind speed {w.wind()['speed']}"
          f"\n{rain}")



HEIGHT = 350
WIDTH = 450


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
                   bg="grey", fg="black",
                   font=('Courier', 8),
                   command= weather_today)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)





root.mainloop()

