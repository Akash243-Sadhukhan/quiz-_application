import datetime
import sys


class QuizeApp:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.correct_count = 0
        self.score = 0
        self.total_points = 0
        self.questions = []

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False

        print("------------------")

        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.score += q.points
                self.correct_count += 1

        return (self.score, self.correct_count, self.total_points)

    def print_results(self, quizetaker, thefile=sys.stdout):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=thefile, flush=True)
        print(f"Result for: {quizetaker} ", file=thefile, flush=True)
        print(f"Date: {datetime.datetime.today()}", file=thefile, flush=True)
        print(f"Correst Questiom: {self.correct_count} out of {len(self.questions)} correctr", file=thefile, flush=True)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=thefile, flush=True)

    def greetings(self):
        print("`````````````````````")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("~~This is a sample questions~~")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print()

    def MenuError(self):
        print("You have not ented any choice")
        print()


class Questions:
    def __init__(self):
        self.correct_answer = " "
        self.is_correct = False
        self.points = 0
        self.text = " "


class QuestionsTF(Questions):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"T: True or F: False {self.text} ")
            _Answer = input("?")

            if len(_Answer) == 0:
                print("sorry its not a valid answer ")
                continue

            _Answer = _Answer.lower()
            if _Answer[0] != "t" and _Answer[0] != "f":
                print("Invalid Input :")
                print(f"T: True or F: False {self.text} ")
                continue

            if _Answer[0] == self.correct_answer:
                self.is_correct = True
            break


class QuestionsMulti(Questions):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"({a.name} {a.text})")

            _Answer = input("?")

            if len(_Answer) == 0:
                print("sorry its not a valid answer ")
                continue

            _Answer = _Answer.lower()
            if _Answer[0] == self.correct_answer:
                self.is_correct = True
            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
