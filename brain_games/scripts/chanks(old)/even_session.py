from random import randint
import prompt
from brain_games import cli


def run_game():
    right_ans_counter = 0
    for right_ans_counter in range(0, 3):
        x = randint(1, 100)
        correct_answer = 'yes' if x % 2 == 0 else 'no'
        print('Question: ' + str(x))
        inputed_answer = prompt.string('Your answer: ')
        if inputed_answer == correct_answer:
            print('Correct!')
            right_ans_counter += 1
        else:
            break
    if right_ans_counter == 3:
        print(f"Congratulations, {cli.inputed_name[0]}!")
    else:
        print(f"'{inputed_answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'.\nLet's try again, {cli.inputed_name[0]}!")
