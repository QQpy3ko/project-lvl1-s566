import random
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(x):
    if x == 1 or not x % 2:
        return False
    for i in range(3, int(math.sqrt(x)), 2):
        if not x % i:
            return False
    return True


def get_question_and_answer():
    a = random.randint(1, 100)

    correct_answer = 'yes' if is_number_prime(a) else 'no'
    question = str(a)

    return question, correct_answer
