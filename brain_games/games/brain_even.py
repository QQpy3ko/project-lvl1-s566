 #!/usr/bin/env python3

import random
from brain_games.games import game_engine


def main():

    descr = 'Answer "yes" if number even otherwise answer "no".'

    def set_question_and_answer():
        x = random.randint(1, 100)
        correct_answer = 'yes' if x % 2 == 0 else 'no'
        question = str(x)
        return question, correct_answer

    game_engine.run_game(descr, set_question_and_answer)


if __name__ == '__main__':
    main()
