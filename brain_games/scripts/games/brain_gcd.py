import random
from brain_games.scripts import game_template


def main():
    game_template.greeting()

    print('Find the greatest common divisor of given numbers.')

    game_template.ask_name()

    def set_question_and_answer(question, correct_answer):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        max_ab = max(a, b)
        min_ab = min(a, b)
        for i in range(min_ab, 0, -1):
            if max_ab % i == 0 and min_ab % i == 0:
                correct_answer = str(i)
                break
        question = str(a) + ' ' + str(b)
        return question, correct_answer

    game_template.run_game(set_question_and_answer)


if __name__ == '__main__':
    main()
