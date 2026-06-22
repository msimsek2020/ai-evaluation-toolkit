questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Capital of Texas?", "answer": "Austin"},
]

def evaluate(model_answers):
    score = 0

    for q, answer in zip(questions, model_answers):
        if answer.lower() == q["answer"].lower():
            score += 1

    return score

sample_answers = ["4", "Austin"]

print("Score:", evaluate(sample_answers))
