import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


root = Tk()
root.geometry('430x300')
root.resizable(False, False)

root.title('Rock Paper Scissors Lizard Spock')

title_label1 = Label(root, text="Hello! I'm Sheldon Cooper and I want you to play with me",
                     font=("Arial", 16))
title_label1.grid(row=0, column=0, columnspan=5, padx=5, pady=10)
title_label2 = Label(root, text="Chose your fighter", font=("Arial", 15))
title_label2.grid(row=1, column=0, columnspan=5, padx=5, pady=10)

sheldons_fighter_label = Label(root, text="", font=("Arial", 14))
sheldons_fighter_label.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

result_label = Label(root, text="", font=("Arial", 16))
result_label.grid(row=5, column=0, columnspan=5, padx=5, pady=10)


def play_rock():
    sheldons_fighter = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    sheldons_fighter_label.config(text=f"My fighter is {sheldons_fighter}")
    if sheldons_fighter == 'Rock':
        result_label.config(text="Dead head!")
    elif sheldons_fighter == 'Paper':
        result_label.config(text='My paper covers your rock! You lose!')
    elif sheldons_fighter == 'Scissors':
        result_label.config(text='Your rock crushes my scissors! You win!')
    elif sheldons_fighter == 'Lizard':
        result_label.config(text='Your rock crushes my lizard! You win!')
    else:
        result_label.config(text='My Spock vaporizes your rock! You lose!')

    root.after(1000, play_again)


def play_paper():
    sheldons_fighter = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    sheldons_fighter_label.config(text=f"My fighter is {sheldons_fighter}")
    if sheldons_fighter == 'Paper':
        result_label.config(text="Dead head!")
    elif sheldons_fighter == 'Rock':
        result_label.config(text='Your paper covers my rock! You win!')
    elif sheldons_fighter == 'Scissors':
        result_label.config(text='My scissors cuts your paper! You lose!')
    elif sheldons_fighter == 'Lizard':
        result_label.config(text='My lizard eats your paper! You lose!')
    else:
        result_label.config(text='Your paper disproves my Spock! You win!')

    root.after(1000, play_again)


def play_scissors():
    sheldons_fighter = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    sheldons_fighter_label.config(text=f"My fighter is {sheldons_fighter}")
    if sheldons_fighter == 'Scissors':
        result_label.config(text="Dead head!")
    elif sheldons_fighter == 'Rock':
        result_label.config(text='My rock crushes your scissors! You lose')
    elif sheldons_fighter == 'Paper':
        result_label.config(text='Your scissors cuts my paper! You win!')
    elif sheldons_fighter == 'Lizard':
        result_label.config(text='Your scissors decapitates my lizard! You win!')
    else:
        result_label.config(text='My Spock smashes your scissors! You lose!')

    root.after(1000, play_again)


def play_lizard():
    sheldons_fighter = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    sheldons_fighter_label.config(text=f"My fighter is {sheldons_fighter}")
    if sheldons_fighter == 'Lizard':
        result_label.config(text="Dead head!")
    elif sheldons_fighter == 'Rock':
        result_label.config(text='My rock crushes your lizard! You lose!')
    elif sheldons_fighter == 'Paper':
        result_label.config(text='Your lizard eats my paper! You win!')
    elif sheldons_fighter == 'Scissors':
        result_label.config(text='My scissors decapitates your lizard! You lose!')
    else:
        result_label.config(text='Your lizard poisons my Spock! You win!')

    root.after(1000, play_again)


def play_spock():
    sheldons_fighter = random.choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    sheldons_fighter_label.config(text=f"My fighter is {sheldons_fighter}")
    if sheldons_fighter == 'Spock':
        result_label.config(text="Dead head!")
    elif sheldons_fighter == 'Paper':
        result_label.config(text='My paper disproves your Spock! You lose!')
    elif sheldons_fighter == 'Scissors':
        result_label.config(text='Your Spock smashes my scissors! You win!')
    elif sheldons_fighter == 'Lizard':
        result_label.config(text='My lizard poisons your Spock! You lose!')
    else:
        result_label.config(text='Your Spock vaporizes my rock! You win!')

    root.after(3000, play_again)


def play_again():
    answer = messagebox.askyesno("Play Again", "Wanna play again?")
    if answer:
        result_label.config(text="")
        sheldons_fighter_label.config(text="")
        title_label1.config(text="")
    else:
        root.quit()


button1 = Button(root, text="Rock", command=play_rock)
button1.grid(row=2, column=0, padx=5, pady=5)

button2 = Button(root, text="Paper", command=play_paper)
button2.grid(row=2, column=1, padx=5, pady=5)

button3 = Button(root, text="Scissors", command=play_scissors)
button3.grid(row=2, column=2, padx=5, pady=5)

button4 = Button(root, text="Lizard", command=play_lizard)
button4.grid(row=2, column=3, padx=5, pady=5)

button5 = Button(root, text="Spock", command=play_spock)
button5.grid(row=2, column=4, padx=5, pady=5)

center_window(root)

root.mainloop()
