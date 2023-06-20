import tkinter as tk
from tkinter import font
from my_OWM import get_weather

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



def display_weather_info(city, label):
    ''' function that take city and transmits information about the weather in label
    city - user input city
    label - a large box where text is displayed '''
    w = get_weather(city)
    label.config(text=w)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: display_weather_info(entry_field.get(), label)# приймає параметр як метод get() у entry_field (маленьке поле введення)
                   ) # label - велике поле виведення


button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14), text="")
label.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()
