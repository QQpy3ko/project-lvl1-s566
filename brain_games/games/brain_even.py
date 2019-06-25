import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def set_question_and_answer():
    x = random.randint(1, 100)
    correct_answer = 'no' if x % 2 else 'yes'
    question = str(x)
    return question, correct_answer
