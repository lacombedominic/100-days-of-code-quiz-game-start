import question_model
import data

question_bank = []
for item in data.question_data:
    new_question = question_model.Question("text", "answer")
    question_bank.append(new_question)
print(question_bank)