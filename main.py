import question_model
import data

question_bank = []
for item in data.question_data:
    new_question = question_model.Question(
        item["text"],
        item["answer"]
    )
    question_bank.append(new_question)
    
for question in question_bank:
    print(question.text, question.answer)