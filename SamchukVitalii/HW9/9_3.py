from pyowm import OWM
import tkinter as tk
from tkinter import font

import requests

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

root = tk.Tk()


def get_weather():
    
    place = entry_field.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={API_KEY}'
    result = requests.get(url)
    weather = result.json()
    info['text'] = f'{weather["name"]}\n{weather["main"]["temp"]}°С\npressure - {weather["main"]["pressure"]}\nhumidity - {weather["main"]["humidity"]}'


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
                   command= get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


info = tk.Label(lower_frame, font=('Courier', 14))
info.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()