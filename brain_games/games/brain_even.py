import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def set_question_and_answer():
    x = random.randint(1, 100)
    correct_answer = 'yes' if x % 2 == 0 else 'no'
    question = str(x)
    return question, correct_answer


