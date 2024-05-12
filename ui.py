from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score = quiz_brain.score
        self.score_label = Label(self.window,
                                 text=f"Score: {self.score}",
                                 fg="white",
                                 bg=THEME_COLOR,
                                 font=("Arial", 12, "bold")
                                 )
        self.score_label.grid(row=0, column=1)

        # Canvas creating
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Question text",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=('Arial', 14, 'italic')
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window,
                                  image=true_img,
                                  highlightthickness=0,
                                  command=lambda: self.check_answer("True")
                                  )
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window,
                                   image=false_img,
                                   highlightthickness=0,
                                   command=lambda: self.check_answer("False")
                                   )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached to the end of questions")
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"

    def check_answer(self, user_answer: str):
        is_right = self.quiz.check_answer(user_answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
