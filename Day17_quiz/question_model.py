import random
import data

class QuestionModel:
    def __init__(self):
        self.num = 0
    def question(self):
        question = random.choice(data.question_data)
        self.num+=1
        return question, self.num


