from tkinter import *
from random import randrange as rnd, choice
import time

#Create child window
def static_window():
    child_root= Toplevel(root)
    child_root.geometry("500x500")
    child_root.title("Statistik")
    

    nik_label = Label(child_root, text='Enter your nick name')
    nik_label.pack()

    nik_entry = Entry(child_root)
    nik_entry.pack()

    add_button = Button(child_root, text='Add record to base')
    add_button.pack()

    new_game_btn = Button(child_root, text='Start new game', command=start_new_game)
    new_game_btn.pack()

    child_root.grab_set()
    child_root.focus_set()
    child_root.wait_window()


def start_new_game():
    global timing, canv
    canv.bind('<Button-1>', click)
    timing = 1000


def new_ball():
    global x,y,r,timing,ball,mis_click
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(25,45)
    
    #виводити рахунок в консоль незручно
    #зручніше його вивести на canvas
    #використавши функцію canv.create_text()
    canv.create_image(0,0, image=bg_img, anchor="nw")
    canv.create_text(80,20, text = "Score: " + str(points), font = 'Arial 15')
    canv.create_text(80,50, text = "Timing: " + str(timing), font = 'Arial 15')
    canv.create_text(80,80, text = "misc_clisk: " + str(mis_click), font = 'Arial 15')
    canv.create_text(80,110, text = "time: " + str(round(total_time/1000)) + ' sec', font = 'Arial 15')   
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=3)
    
    root.after(timing,new_ball)


def click(event):
    global points,r,timing,mis_click

    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        timing -= 10
        # Видаляюмо фігуру
        canv.delete(ball)
        #root.after(timing,new_ball)
    else:
        mis_click += 1
        #root.after(timing,new_ball)


#Таймер на 1хв    
def my_timer():
    global timing, tm
    # msg = Message(root, text=f'Time left, mis_clik {mis_click}, catched ball {points}')
    # msg.pack(fill=BOTH)


    canv.unbind("<Button-1>")
    timing = 10000000000000000

    new_game_btn = Button(root, text='Start new game', command=start_new_game)
    new_game_btn.pack()    
    #static_window()
   

# створюємо вікно
root = Tk()

root.geometry('800x600')
# задаємо назву вікна
root.title("Joe's balls")

bg_img = PhotoImage(file="img/bg_main.gif")

canv=Canvas(root)
canv.pack(fill=BOTH,expand=True)

colors = ['red','beige','azure','green','blue']


mis_click = 0
timing = 1000
points = 0
#One minute contain 60 000 ms
total_time = 6000

new_ball()

canv.bind('<Button-1>', click)

#After finish show stop msg for user

root.after(total_time, my_timer)


mainloop()
