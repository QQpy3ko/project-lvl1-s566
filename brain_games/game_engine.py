import prompt
from brain_games import cli


def greet():
    print("Welcome to the Brain Games!")


def run_game(game):

    greet()

    print(game.DESCRIPTION)

    gamer_name = cli.ask_name()

    for _ in range(0, 3):

        question, correct_answer = game.get_question_and_answer()
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
