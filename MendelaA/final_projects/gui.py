from tkinter import *
import variables




class Window():
    """
    Class for creatin main game window
    """
    def __init__(self, width, height, title='Joe Balls', resizable=(False, False)):
        self.root = Tk()
        self.root.geometry(f'{width}x{height}')
        self.root.resizable(resizable[0], resizable[1])

        self.canv = Canvas(self.root, background='green')
           
        self.label = Label(self.root, text="Label")

    def run(self):
        #Draw widgets
        self.draw_canvas()
        self.draw_labe()
        #Run main loop
        self.root.mainloop()

    def draw_canvas(self):
        self.canv.pack(fill=BOTH,expand=True)
    
    def draw_labe(self):
        self.label.pack()




if __name__ == '__main__':
    #bg_img = PhotoImage(file="img/bg_main.gif") 
    window = Window(800,600)
    window.run()
    
    #window.canv.create_image(0,0, image=bg_img, anchor="nw")