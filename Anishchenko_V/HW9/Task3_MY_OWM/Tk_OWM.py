import tkinter as tk
from tkinter import font
import OWM

HEIGHT = 500
WIDTH = 650


root = tk.Tk()
result = 'Weather desription will appear here'


def get_weather(location):
    try:
        result = OWM.weather(location)
        label.config(text=result)
    except:
        label.config(text='Incorrect input. Try again')


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
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 12),
                 text='', anchor='w', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)
label.config(text=result)

root.mainloop()
