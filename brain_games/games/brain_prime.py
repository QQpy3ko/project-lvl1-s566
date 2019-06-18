 #!/usr/bin/env python3

import random
import math
from brain_games.games import game_engine


def main():

    descr = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def set_question_and_answer():
        x = random.randint(1, 100)
        if x == 1:
            correct_answer = 'no'
        else:
            for i in range(2, int(math.sqrt(x))+1):
                if not x % i:
                    correct_answer = 'no'
                    break
            else:
                correct_answer = 'yes'
        question = str(x)
        return question, correct_answer

    game_engine.run_game(descr, set_question_and_answer)


if __name__ == '__main__':
    main()
