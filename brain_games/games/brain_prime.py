import random
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def set_question_and_answer():
    x = random.randint(1, 100)
    if x == 1 or not x % 2:
        correct_answer = 'no'
    else:
        for i in range(3, int(math.sqrt(x)), 2):
            if not x % i:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    question = str(x)
    return question, correct_answer
