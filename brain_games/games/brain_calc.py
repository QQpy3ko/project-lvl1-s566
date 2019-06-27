import operator
import random

OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }

DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    random_operator_key = random.choice(list(OPERATORS))

    question = f"{a} {random_operator_key} {b}"
    correct_answer = str(OPERATORS[random_operator_key](a, b))

    return question, correct_answer
