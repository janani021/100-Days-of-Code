from data import question_data
from question_model import QuestionModel

question_model=QuestionModel()
class Quizbrain:

    def __init__(self):
        self.correct_answer = 0
    def check_answer(self,question,answer):
        if (question['correct_answer']==answer):
            print("You got it right!")
            flag=True
        else:
            print("That's wrong")
            flag=False
        print(f"The correct answer was: {question['correct_answer']}")
        return flag

    def score(self):
        self.correct_answer += 1
        return self.correct_answer
