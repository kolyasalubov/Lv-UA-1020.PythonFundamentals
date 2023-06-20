import tkinter as tk

import my_OWM

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
                   bg="gray", fg="black",
                   font=('Courier', 8),
                   command=lambda: display_result())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


def display_result():
    city = entry_field.get()
    result = my_OWM.get_weather(city)
    label.config(text="Result: \n" + str(result), wraplength=200)


result_label = tk.Label(root, text="")

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


result_label.pack()
root.mainloop()
