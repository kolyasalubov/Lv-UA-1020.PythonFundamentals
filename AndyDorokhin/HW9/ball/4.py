from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Caught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
############################################################
def new_ball():
    global x,y,r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    # canv.create_text(20,20,text=str(points), font = 'Arial 20')
    
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)
###################################################################

 # функція, яка провіряє, чи не лежить 
 # точка event.x,event.y дальше, ніж r 
 # від точки x,y. Для цього, з допомогою
 # теореми Піфагора ми знаходимо
 # відстань між двома точками і порівнюємо 
 # з радіусом круга.
 #  
 # якщо відстань(гіпотенуза) більша за радіус 
 # круга, то клік відбувся зовні круга
 #  
 # якщо відстань(гіпотенуза) менша за радіус 
 # круга, то клік відбувся всередині круга    
     
def click(event):
    global points
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1 #змінна підрахунку кількості співпадінь (вгадувань)
 
points = 0
new_ball()
canv.bind('<Button-1>', click)
 
mainloop()
