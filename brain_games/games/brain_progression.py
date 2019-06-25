import random

DESCRIPTION = 'What number is missing in the progression?'


def set_question_and_answer():
    first_elem = random.randint(0, 10)
    hidden_elem = random.randint(0, 10)
    step = random.randint(1, 10)
    correct_answer = str(first_elem + hidden_elem * step)
    crypted_list = [str(first_elem)]
    for i in range(1, 10):
        if i == hidden_elem:
            crypted_list.append('..')
        else:
            crypted_list.append(str(first_elem + i * step))

    question = ' '.join(crypted_list)

    return question, correct_answer
