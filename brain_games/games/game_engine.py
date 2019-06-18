 #!/usr/bin/env python3

import prompt
from brain_games.scripts import cli


def greeting():
    print("Welcome to the Brain Games!")


# here appears game-task in game-name


def ask_name():
    return cli.run()


def run_game(descr, question_and_answer):

    greeting()

    print(descr)

    gamer_name = ask_name()

    right_ans_counter = 0
    for right_ans_counter in range(0, 3):

        question, correct_answer = question_and_answer()
        print('Question: ' + question)
        inputed_answer = prompt.string('Your answer: ')
        if inputed_answer == correct_answer:
            print('Correct!')
            right_ans_counter += 1
        else:
            print(f"'{inputed_answer}' is wrong answer ;(. Correct answer was "
f"'{correct_answer}'.\nLet's try again, {gamer_name}!")
            break
  
    else:
        print(f"Congratulations, {gamer_name}!")
        
