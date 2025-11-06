from data import question_data
from question_modal import Model
from question_mind import Mind
from data2 import question_data2


# print(question_data2["results"][0]["correct_answer"])

# for quesstions in question_data2["results"]:
#     print(quesstions["question"])


bankq = []
banka = []


for questions in question_data2["results"]:
    question = Model(questions["question"], questions["correct_answer"])

    bankq.append(question.quest)
    banka.append(question.answer)

quiz = Mind(banka, bankq)
quiz.next()

while quiz.again():
    quiz.next()

print(f"Final score is {quiz.score}")




