from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.label = Label(text='score: 0', bg=THEME_COLOR, font=('Arial', 15, 'bold'), fg='white')
        self.label.grid(row=0, column=1)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='some question text', fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=self.right_image, command=self.right_answer)
        self.right_button.grid(row=2, column=0)

        self.wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=self.wrong_image, command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
