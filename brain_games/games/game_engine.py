import prompt
from brain_games.scripts import cli


def greeting():
    print("Welcome to the Brain Games!")


def ask_name():
    return cli.run()


def run_game(game):

    greeting()

    print(game.DESCRIPTION)

    gamer_name = ask_name()

    for right_ans_counter in range(0, 3):

        question, correct_answer = game.set_question_and_answer()
        print('Question: ' + question)
        inputed_answer = prompt.string('Your answer: ')
        if inputed_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{inputed_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.\nLet's try again, {gamer_name}!")
            break

    else:
        print(f"Congratulations, {gamer_name}!")
