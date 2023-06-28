from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#53868B"  #https://www.webucator.com/article/python-color-constants-module/


class QuizGameWindow():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quiz Game")

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Hello",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label = Label(text="Score: 0",
                                 fg="white",
                                 bg=THEME_COLOR,
                                 highlightthickness=0,
                                 font=("Arial", 20, "italic"))
        self.score_label.grid(column=1, row=0)

        flag = PhotoImage(file="images/Flag_of_Ukraine.png")
        self.label_flag = Label(image=flag, height=80, width=150)
        self.label_flag.grid(row=0, column=0)


        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                        font=("Arial", 30, "italic"),
                        text= f"The end of the quiz.\nYour score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


