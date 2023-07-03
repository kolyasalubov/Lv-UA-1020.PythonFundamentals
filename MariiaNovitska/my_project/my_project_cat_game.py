from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox as mb
import time
import webbrowser

root = Tk()                         # створюєм корневий об'єкт - вікно
root.geometry('400x330')            # встановлюємо розміри вікна
root.title("CAT")                   # встановлюємо заголовок вікна

icon = PhotoImage(file="D:\\Python SoftServe\\Lesson 2\\Lv-UA-1020.PythonFundamentals\\MariiaNovitska\\my_project\\iconCat.png")  # альтернативна опція встановлення іконки
root.iconphoto(False, icon)  # альтернативна опція встановлення іконки

root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])
 
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2 
w = w - width_root // 2
h = h - height_root // 2
root.geometry('+{}+{}'.format(w, h))

logo = PhotoImage(file="D:\\Python SoftServe\\Lesson 2\\Lv-UA-1020.PythonFundamentals\\MariiaNovitska\\my_project\\cat.png")  # створюємо об'єкт зображення
logo1 = Label(image=logo)  # створюємо об'єкт зображення https://www.pythontutorial.net/tkinter/tkinter-photoimage/

game = True  # умова продовження гри
healthCat = 20  # "здоров'я,"
leisureCat = 20  # leisure - "задоволення"
while game:
    def update_clock():
        ''' функція, яка відповідає за оновлення ігрової ситуації раз на секунду '''
        global healthCat  
        global leisureCat  
        global game
        if healthCat <= 0 or leisureCat <= 0:
            answer = mb.askyesno(title="You lost", message="Do you want to play again?") #ПОФІКСИЛА ЗАЦИКЛЕННЯ ВІКОНЕЧКА ВИХОДУ
            if answer == True:
                healthCat += 50
                leisureCat += 50
            else:
                game = False
                quit()
        elif healthCat >= 100 and leisureCat >= 100:
            answer2 = mb.askyesno(title="You win", message="Do you want to play again?")
            if answer2 == True:
               healthCat -= 50
               leisureCat -= 50
            else:
                quit()
        
        now = time.strftime("%H:%M:%S")
        root.after(1000, update_clock)
        root.after(1000, heppimin)






    def heppimin():
        global healthCat  
        global leisureCat  
        if (healthCat - 3) <= 0 or (leisureCat - 3) <= 0:   #ПОФІКСИЛА ВІД'ЄМНІ ЗНАЧЕННЯ ПРОЦЕНТІВ
            healthCat = healthCat - (3 + (healthCat - 3))
            leisureCat = leisureCat - (3 + (leisureCat - 3))
        elif healthCat >= 100 and leisureCat >= 100:        #ПОФІКСИЛА ЗНАЧЕННЯ ПРОЦЕНТІВ, БІЛЬШЕ 100%
            l1.configure(text="health - 100%")   
            l2.configure(text="leisure - 100%")
            return
        else:
            healthCat = healthCat - 3  # кожної ітерації параметр "здоров'я," зменшується на 3
            leisureCat = leisureCat - 3  # кожної ітерації параметр "задоволення" зменшується на 3
        l1.configure(text="health - " + str(healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")  # змінюємо налаштування текстової мітки "задоволення"


    def health():
        global healthCat
        global leisureCat
        if healthCat + 10 > 100:
            healthCat = healthCat + (100-healthCat)
        else:
            healthCat = healthCat + 10
            leisureCat = leisureCat - 2
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="your cat is healh")
        



    def leisure():
        global healthCat
        global leisureCat
        if leisureCat + 10 > 100:
            leisureCat = leisureCat + (100-leisureCat)
        else:
            healthCat = healthCat - 2
            leisureCat = leisureCat + 10
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="your cat is laisure")
        

    
    def my_quit():
        global game
        game = False
        answer3 = mb.askyesno(title="Exit", message="Do you want to exit?")
        if answer3 == True:
            quit()
        else:
            game = True

    def cats():
        webbrowser.open_new("https://www.freepik.com/free-photos-vectors/cat-art")


    label2 = Label(width=27, height=3, text="It is your Cat", font="Arial")
    b1 = ttk.Button(width=15, text="feed", command=health)  # годувати
    b2 = ttk.Button(width=15, text="caress", command=leisure)  # пестити
    b3 = ttk.Button(width=15, text="train", command=health)  # виховувати, тренувати
    b4 = ttk.Button(width=15, text="play", command=leisure)  # грати
    b5 = ttk.Button(width=15, text="Want more cats!", command=cats)  # вихід
    l1 = Label(width=20, height=3, text="health - " + str(healthCat) + "%")  # здоров'я,
    l2 = Label(width=20, height=2, text="leisure - " + str(leisureCat) + "%")  # задоволення, дозвілля
    l3 = Label(width=20, height=2, text="your cat is alive")  # здоровий

    label2.grid(row=0, column=2, columnspan=3, rowspan=2)
    b1.grid(row=2, column=0)
    b2.grid(row=3, column=0)
    b3.grid(row=4, column=0)
    b4.grid(row=5, column=0)
    b5.grid(row=9, column=3)
    l1.grid(row=6, column=0)
    l2.grid(row=7, column=0)
    l3.grid(row=7, column=3)
    logo1.grid(row=2, column=2, columnspan=5, rowspan=5)

    update_clock()
    root.mainloop()  # Для відображення вікна та взаємодії з користувачем у вікна викликається метод mainloop()
