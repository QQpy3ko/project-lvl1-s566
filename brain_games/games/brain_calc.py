 #!/usr/bin/env python3

import operator
import random
from brain_games.games import game_engine

OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }


def main():
    descr = "What is the result of the expression?"

    def set_question_and_answer():
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        random_operator_key = random.choice(list(OPERATORS))

        question = f"{str(a)} {random_operator_key} {str(b)}"
        correct_answer = str(OPERATORS[random_operator_key](a, b))
        
        return question, correct_answer

    game_engine.run_game(descr, set_question_and_answer)


if __name__ == '__main__':
    main()
