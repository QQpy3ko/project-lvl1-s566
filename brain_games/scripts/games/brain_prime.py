import random
from brain_games.scripts import game_template


def main():
    game_template.greeting()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    game_template.ask_name()

    def set_question_and_answer(question, correct_answer):
        x = random.randint(1, 100)
        if x == 1:
            correct_answer = 'no'
        else:
            for i in range(2, x):
                if x % i == 0:
                    correct_answer = 'no'
                    break
            else:
                correct_answer = 'yes'
        question = str(x)
        return question, correct_answer

    game_template.run_game(set_question_and_answer)


if __name__ == '__main__':
    main()
