from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain

# question_bank=[]
# for obj in question_data:
#     question_bank.append(Question(obj['text'], obj['answer']))

# simple data
# question_bank= [ Question(obj['text'], obj['answer']) for obj in question_data ]
question_bank= [ Question(obj['question'], obj['correct_answer']) for obj in question_data ]


quizz = Quiz_Brain(question_bank)

while(not quizz.is_finished()):
    quizz.next_question()

print("... finished !")
print(f'Final Score is : {quizz.points}/{quizz.question_number}')

