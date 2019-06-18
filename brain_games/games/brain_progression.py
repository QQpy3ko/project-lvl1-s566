#!/usr/bin/env python3

import random
from brain_games.games import game_engine


def main():

    descr = 'What number is missing in the progression?'

    def set_question_and_answer():
        first_elem = random.randint(0, 10)
        hidden_elem = random.randint(0, 10)
        step = random.randint(1, 10)
        true_list = [str(first_elem)]
        crypted_list = [str(first_elem)]
        counter = step
        for i in range(0, 9):
            true_list.append(str(first_elem + counter))
            crypted_list.append(str(first_elem + counter))
            counter += step
            if i == hidden_elem:
                crypted_list[hidden_elem] = '..'

        # crypted_list = list(map(str, true_list))
        # crypted_list[hidden_elem] = '..'
        question = ' '.join(crypted_list)
        correct_answer = true_list[hidden_elem]
        return question, correct_answer

    game_engine.run_game(descr, set_question_and_answer)


if __name__ == '__main__':
    main()
