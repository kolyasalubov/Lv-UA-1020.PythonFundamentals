import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    location = entry_field.get()
    observation = mgr.weather_at_place(location)
    w = observation.weather

    report_weather = f"Current weather: {w.detailed_status}\n"
    report_temp = f"Temperature, °C: {w.temperature('celsius')['temp']},\nfeels like: {w.temperature('celsius')['feels_like']}\n"
    report_wind = f"Wind speed, m/sec: {w.wind()['speed']}\n"
    report_humidity = f"Humidity, %: {w.humidity}\n"
    report_rain = f"Rain, mm: {w.rain.get('1h', 0)}\n"
    report_clouds = f"Clouds, %: {w.clouds}\n"
    full_report = report_weather + report_temp + report_wind + report_humidity + report_rain + report_clouds
    label['text'] = full_report
    label['text'].pack()


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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 12))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

      
    
    

