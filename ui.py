THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.text_area = Canvas(height=250, width=300, bg="white")
        self.text_area.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.text_area.create_text(150, 125, text="Hello", font=("Arial", 20, "italic"), width=280)

        self.check_image = PhotoImage(file="images/true.png")
        self.cross_image = PhotoImage(file="images/false.png")

        self.check_button = Button(image=self.check_image, highlightthickness=0, command=self.correct)
        self.check_button.grid(row=2, column=0)

        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=self.wrong)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.text_area.config(bg="green")
        else:
            self.text_area.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.text_area.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.text_area.itemconfig(self.text, text=q_text)
        else:
            self.text_area.itemconfig(self.text, text="You have reached the end of the quiz!")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

