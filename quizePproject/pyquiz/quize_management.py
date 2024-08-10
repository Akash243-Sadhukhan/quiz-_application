import os.path
import os
import datetime
from quiz_perser import QuizePerser


class QuizeManager:
    def __init__(self, quizefolder) :
        #to store the quizefile
        self.quizefolder = quizefolder
        #to store the most recent opend quize
        self.the_quize = None
        #to inisiallize the collection of quizes
        self.quizzes = dict()
        #to store the result of the most recent quize
        self.results = None
        #to store the name of the person
        self.quizetaker = "" 

        #to make sure the quizefolder exits
        if not os.path.exists(self.quizefolder):
            raise FileNotFoundError("The quiz folder does not exist")
        #to build the quize list
        self._build_quiz_list()
    
    def _build_quiz_list(self):
        dircontent = os.scandir(self.quizefolder)
        #to parse the xml file in the quize folder
        for i,f in enumerate(dircontent):
            if f.is_file():
                parser = QuizePerser()
                self.quizzes[i+1] = parser.Perser_quize(f)


    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print(f"({k}): {v.name}")

    def take_quiz(self, quizid, username):
        self.quizetaker = username
        self.the_quize = self.quizzes[quizid]
        self.results = self.the_quize.take_quiz()
        return self.results
    
    def print_results(self):
        self.the_quize.print_results(self.quizetaker)
            

    def save_results(self):
        current_date = datetime.date.today().strftime("%y_%m_%d")
        file_name = f"Quiz_result_{current_date}.txt"
        n = 0
        while os.path.exists(file_name):
            file_name = f"Quiz_result_{current_date}-{n}.txt"
            n += 1
        with open(file_name, "w") as f:
            self.the_quize.print_results(self.quizetaker, f)
            print(f)
        


if __name__ == "__main__":
    print("is file" if os.path.exists("quize_xml_files") else "is not file")
    qm = QuizeManager("quize_xml_files")
    qm.list_quizzes()
    qm.save_results()