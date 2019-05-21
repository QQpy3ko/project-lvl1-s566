import prompt
from brain_games import cli


def greeting():
    print("Welcome to the Brain Games!")


# here appears game-task in game-name


def ask_name():
    cli.run()


def run_game(x):
    right_ans_counter = 0
    question = ''
    correct_answer = ''

    for right_ans_counter in range(0, 3):

        question, correct_answer = x(question, correct_answer)
        print('Question: ' + question)
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
