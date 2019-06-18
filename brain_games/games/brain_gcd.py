 #!/usr/bin/env python3

import random
from brain_games.games import game_engine


def main():

    descr = "Find the greatest common divisor of given numbers."


    def set_question_and_answer():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        
        question = f"{str(a)} {str(b)}"

        while a and b:
            if a > b:
                a = a % b
            else:
                b = b % a
        
        correct_answer = str(a + b)
        

        return question, correct_answer

    game_engine.run_game(descr, set_question_and_answer)


if __name__ == '__main__':
    main()
