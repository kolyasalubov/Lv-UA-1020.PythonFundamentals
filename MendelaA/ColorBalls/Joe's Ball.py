from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Joe's balls")

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

def new_ball():
    global x,y,r,timing,ball,mis_click
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(25,50)
    
    #виводити рахунок в консоль незручно
    #зручніше його вивести на canvas
    #використавши функцію canv.create_text()
    canv.create_text(80,20, text = "Score: " + str(points), font = 'Arial 15')
    canv.create_text(80,50, text = "Timing: " + str(timing), font = 'Arial 15')
    canv.create_text(80,80, text = "misc_clisk: " + str(mis_click), font = 'Arial 15')
    canv.create_text(80,110, text = "time: " + str(round(total_time/1000)) + ' sec', font = 'Arial 15')   
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(timing,new_ball)

     
def click(event):
    global points,r,timing,mis_click
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        timing -= 10
        # Видаляюмо фігуру
        canv.delete(ball)
    else:
        mis_click += 1


#Таймер на 1хв    
def my_timer():
    global timing
    msg = Message(root, text=f'Time left, mis_clik {mis_click}, catched ball {points}')
    msg.pack(fill=BOTH)

    canv.unbind("<Button-1>")
    timing = 0 

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
