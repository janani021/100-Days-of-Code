import data
from question_model import QuestionModel
from quiz_brain import Quizbrain

question_model = QuestionModel()
quiz_brain = Quizbrain()

flag=True
total = (len(data.question_data))

while(flag):
    question,num=question_model.question()
    print(f"Q.{num} {question['question']} (True/False):")
    answer=input()
    answer.capitalize()
    data.question_data.remove(question)
    if (quiz_brain.check_answer(question,answer)):
        correct_answer=quiz_brain.score()
    else:
        correct_answer=quiz_brain.correct_answer
    print(f"Your current score is: {correct_answer}/{num}")
    if(num>=total):
        flag=False