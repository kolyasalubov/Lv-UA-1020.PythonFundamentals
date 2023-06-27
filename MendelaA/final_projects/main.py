from gui import Window
from random import randrange as rnd, choice
import sqlite3
from tkinter import *

#######################     VARIABLES POLL   #########################################
colors = ['red','beige','azure','green','blue']
mis_click = 0
timing = 1000
points = 0
#One minute contain 60 000 ms
total_time = 6000
#bg_img = PhotoImage(file="img/bg_main.gif")
#######################     VARIABLES POLL   #########################################

def new_ball():
    global x,y,r,timing,ball,mis_click,total_time
        
    window.canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(25,45)
            
    #виводити рахунок в консоль незручно
    #зручніше його вивести на canvas
    #використавши функцію canv.create_text()
    #window.create_image(0,0, image=bg_img, anchor="nw")
    window.canv.create_text(80,20, text = "Score: " + str(points), font = 'Arial 15')
    window.canv.create_text(80,50, text = "Timing: " + str(timing), font = 'Arial 15')
    window.canv.create_text(80,80, text = "misc_clisk: " + str(mis_click), font = 'Arial 15')
    window.canv.create_text(80,110, text = "time: " + str(round(total_time/1000)) + ' sec', font = 'Arial 15')   
    ball = window.canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=3)

    window.after(timing,new_ball)


window = Window(800,600)
window.run()




