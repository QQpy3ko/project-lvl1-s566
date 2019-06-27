import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(x, y):
    while x and y:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x, y


def get_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    question = f"{a} {b}"

    first_gcd_item, second_gcd_item = find_gcd(a, b)

    correct_answer = str(first_gcd_item + second_gcd_item)

    return question, correct_answer
