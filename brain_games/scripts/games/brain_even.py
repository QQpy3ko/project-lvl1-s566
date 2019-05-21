import random
from brain_games.scripts import game_template


def main():
    game_template.greeting()

    print('Answer "yes" if number even otherwise answer "no".')

    game_template.ask_name()

    def set_question_and_answer(question, correct_answer):
        x = random.randint(1, 100)
        correct_answer = 'yes' if x % 2 == 0 else 'no'
        question = str(x)
        return question, correct_answer

    game_template.run_game(set_question_and_answer)


if __name__ == '__main__':
    main()