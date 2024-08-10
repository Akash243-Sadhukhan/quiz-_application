import xml.sax
from quize import *
from enum import Enum, unique

# unique function used to find the unique function in an arry or list and return the unique elements only

@unique
class QuizePerserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5

class QuizePerser(xml.sax.ContentHandler):
    def __init__(self) :
        self.new_quize = QuizeApp()
        self._perser_state = QuizePerserState.IDLE
        self._current_question = None
        self._current_answer = None

    def Perser_quize(self, quizepath):
        quizetext = ""
        with open(quizepath, "r", encoding="latin-1") as quizefile:  # Or try another encoding like "windows-1252"
            if quizefile.mode == "r":
                quizetext = quizefile.read()

        xml.sax.parseString(quizetext, self)

        return self.new_quize

    def startElement(self, tagname, attrs ):
        if tagname == "QuizML":
            self._perser_state = QuizePerserState.PARSE_QUIZ
            self.new_quize.name = attrs["name"]
        elif tagname == "Description" :
            self._perser_state = QuizePerserState.PARSE_DESCRIPTION
        elif tagname == "Question":
            self._perser_state = QuizePerserState.PARSE_QUESTION
            if (attrs["type"] == "multichoice"):
                self._current_question = QuestionsMulti()
            if (attrs["type"] == "tf"):
                self._current_question = QuestionsTF()
            self._current_question.points = int(attrs["points"])
            self.new_quize.total_points += self._current_question.points
        elif tagname == "QuestionText":
            self._perser_state = QuizePerserState.PARSE_QUEST_TEXT
            self._current_question.correct_answer = attrs["answer"]
        elif tagname == "Answer":
            self._current_answer = Answer()
            self._current_answer.name = attrs["name"]
            self._perser_state = QuizePerserState.PARSE_ANSWER


    def endElement(self, tagname):
        if tagname == "QuizML":
            self._perser_state = QuizePerserState.IDLE

        elif tagname == "Discription":
            self._perser_state = QuizePerserState.PARSE_QUIZ

        elif tagname == "Question":
            self.new_quize.questions.append(self._current_question)
            self._perser_state = QuizePerserState.PARSE_QUIZ
        elif tagname =="QuestionText":
            self._perser_state = QuizePerserState.PARSE_QUESTION
        elif tagname == "Answer":
            self._current_question.answers.append(self._current_answer)
            self._perser_state = QuizePerserState.PARSE_QUESTION

    def characters(self, chars):
        if self._perser_state == QuizePerserState.PARSE_DESCRIPTION:
            self.new_quize.description += chars
        elif self._perser_state == QuizePerserState.PARSE_QUEST_TEXT:
            self._current_question.text += chars
        elif self._perser_state == QuizePerserState.PARSE_ANSWER:
            self._current_answer.text += chars

    
# if __name__ == '__main__':
#     app = QuizePerser()
#     qz = app.Perser_quize("pyquiz/quizers/quizers 16-39-29-621/questions_basics/quizers_xml_files/SampleQuiz.xml")
#     print(qz.name)
#     print(qz.description)
#     print(len(qz.questions))
#     print(qz.total_points)
#     for q in qz.questions:
#         print(f"Question: {q.text}")
        