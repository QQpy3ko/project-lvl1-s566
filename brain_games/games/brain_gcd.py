import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(x, y):
    while x and y:
        if x > y:
            x = x % y
        else:
            y = y % x
    gcd = str(x + y)
    return gcd


def get_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f"{a} {b}"

    correct_answer = str(find_gcd(a, b))

    return question, correct_answer
