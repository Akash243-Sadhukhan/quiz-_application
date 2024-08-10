from quize_management import QuizeManager


class QuizeMain:
    QUIZE_FOLDER = "quize_xml_files"

    def __init__(self):
        self.username = ""
        self.qm = QuizeManager(QuizeMain.QUIZE_FOLDER)

    def startup(self):

        self.greetings()
        self.username = input("what is your name: ")
        print(f"Welcome : {self.username} ")

    def greetings(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~welcome, to the quize~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

    def goodbye(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Thank you for taking the quiz : {self.username}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
    def menu_header(self):
        print("Plese seclect a option")
        print("M: Repeat this meanu")
        print("L: list the quizes")
        print("T: Take the Quize")
        print("E: exit the program")
        print()

    def menu_error(self):
        print("Your input is invalid, plese try again")

    def meanu(self):
        self.menu_header()
        _response = ""
        while (True):
            _response = input("enter your choice : ")
            _response = _response.capitalize()
            if _response[0] == 'E':
                self.goodbye()
                break
            elif _response[0] == 'M':
                self.menu_header()
                continue
            elif _response[0] == 'L':
                print("______________________________")
                self.qm.list_quizzes()
                print("______________________________")
                continue

            elif _response[0] == 'T':
                try:
                    quiznum = int(input("Enter the number of quize"))

                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                    ch = input("Press 'Y' to save the result and 'N' to enter the menu: ")
                    ch = ch.capitalize()
                    if len(ch)>0 and ch[0] == 'Y':
                        self.qm.save_results()

                except:
                    self.menu_error()

            else:
                self.menu_error()

    def run(self):
        self.startup()
        self.meanu()


if __name__ == "__main__":
    app = QuizeMain()
    app.run()
