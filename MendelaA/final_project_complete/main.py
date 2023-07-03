from tkinter import *
from random import randrange as rnd, choice
import sqlite3

### VARIABLE ####
mis_click = 0
timing = 1000
points = 0
total_time = 6000 #One minute contain 60 000 ms
colors = ['red','beige','azure','green','blue'] #Balls color list
### VARIABLE ####

### FUNCTIONS ###

def new_ball():
    """
    This function create random ball, 
    draw in lef top conor informatio like Score, Timing, Misc_clisk, Time
    and in the end call themself like recursion.
    """
    global x,y,r,timing,ball,mis_click,total_time
        
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
    canv.create_text(80,80, text = "Misc_clisk: " + str(mis_click), font = 'Arial 15')
    canv.create_text(80,110, text = "Time: " + str(round(total_time/1000)) + ' sec', font = 'Arial 15')   
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=3)
    root.after(timing,new_ball)


def click(event):
    """
    This functio prodive mouse click behaviours like
    if you cath the ball you get +1 to Score + increased ball 
    appear spped, otherway +1 to mis_clik.
    """
    
    global points,y,r,timing,mis_click

    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        timing -= 10
        canv.delete(ball) # Delete the bal
    else:
        mis_click += 1


def my_timer():
    """
    This functions provide simple end form,
    user can view TOP user and can save own progress
    """

    global show_score_btn,score_list,save_btn
    canv.unbind("<Button-1>") #Disable binding mouse button

    nik_label = Label(root, text="Enter yout NikName")
    nik_label.pack(pady=1)

    show_score_btn = Entry(root)
    show_score_btn.pack(pady=1)

    save_btn = Button(root, text='Save score', command=db_add)
    save_btn.pack(pady=1)

    top_label = Label(root, text="Top USER IS !")
    top_label.pack(pady=1)

    score_list = Label(root)
    score_list.pack(pady=1)
    
    quit_btn = Button(root, text='Quit game', command=root.quit)
    quit_btn.pack(pady=1)

    db() #Initialize our DB
    db_get() #Get TOP 1 and change label

def db():
    """
    This function create connect to db and create table if it not exist
    """

    #Connect to db
    with sqlite3.connect('db.db') as conn:
        #Cursor
        cursor = conn.cursor()

        #Create table
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS "results" (
                        "id"	INTEGER NOT NULL UNIQUE,
                        "nick_name"	TEXT NOT NULL,
                        "scores"	INTEGER NOT NULL,
                        "mis_clisk"	INTEGER NOT NULL,
                        PRIMARY KEY("id" AUTOINCREMENT));
                        ''')
        


def db_get():
    """
    This function add record to our db
    """

    global points, mis_click,show_score_btn,save_btn
    with sqlite3.connect('db.db') as conn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nick_name, max(scores) FROM results')
        result = cursor.fetchall()

        result = f'{result[0][0]} has catched {result[0][1]} balls' #Make pretty str

        score_list.config(text = result) #Change Label


def db_add():
    """
    This function get data from db
    """

    global points, mis_click,show_score_btn,save_btn
    with sqlite3.connect('db.db') as conn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO results ("nick_name", "scores", "mis_clisk") VALUES (?, ?, ?)',
                    (show_score_btn.get(), points, mis_click))
        conn.commit()# Write changes
    
    save_btn.config(state='disabled')
    db_get() #Call to update TOP 1
### FUNCTIONS ###

### MAIN CODE ###
root = Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title("Joe's balls")

bg_img = PhotoImage(file="img/bg_main.gif")

canv=Canvas(root) #Create Canvas
canv.pack(fill=BOTH,expand=True)

new_ball() #Call func new_ball to create new bal :) and draw info
canv.bind('<Button-1>', click) #Bind mouse button

root.after(total_time, my_timer) #Time, call the end of game
root.mainloop()
### MAIN CODE ###