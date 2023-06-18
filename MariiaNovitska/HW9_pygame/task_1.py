import tkinter as tk
from random import randint

HEIGHT = 250
WIDTH = 350

rand_int = randint(1,100)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Guess number")
root.resizable(width=False, height=False)
canvas.pack()

value_count = tk.IntVar()
counter = 1


def gues_number(event):
    global counter
    value = value_count.get()

    if counter > 9:
        label_1["text"] = "You lost!"
    elif value == rand_int:
        label_1["text"] = "You won!"
    elif value > rand_int:
        label_1["text"] = "Try lower number"
        counter +=1
        label_2["text"] = f"Attempt: {counter}"
    else:
        label_1["text"] = "Try higer number"
        counter +=1
        label_2["text"] = f"Attempt: {counter}"

    user_input.delete(0, 20)


frame = tk.Frame(root, bg="DarkSeaGreen2", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

user_input = tk.Entry(frame, font=('Courier', 12), textvariable=value_count)
user_input.place(relx=0, rely=0, relwidth=0.65, relheight=1)

my_button = tk.Button(frame, text="Enter")
my_button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
my_button.bind('<Button-1>', gues_number)

frame_2 = tk.Frame(root, bg="SlateBlue4", bd=5)
frame_2.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.35, anchor='n')

label_1 = tk.Label(frame_2, font=('Courier', 12), text="Try to guess number \nbetween 1 and 100. \nYou have 10 attempts")
label_1.place(relx=0, rely=0, relwidth=1, relheight=1)


frame_3 = tk.Frame(root, bg="royal blue", bd=5)
frame_3.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')

label_2 = tk.Label(frame_3, font=('Courier', 12), text=f"Attempt: 1")
label_2.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

