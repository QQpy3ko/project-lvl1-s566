import random
from brain_games.scripts import game_template


def main():
    game_template.greeting()

    print('What number is missing in the progression?')

    game_template.ask_name()

    def set_question_and_answer(question, correct_answer):
        first_elem, hidden_elem = (random.randint(0, 9) for i in range(0, 2))
        step = random.randint(1, 10)
        true_list = [first_elem]
        for i in range(0, 9):
            true_list.append(true_list[-1] + step)
        crypted_list = list(map(str, true_list))
        crypted_list[hidden_elem] = '..'
        question = ' '.join(crypted_list)
        correct_answer = str(true_list[hidden_elem])
        return question, correct_answer

    game_template.run_game(set_question_and_answer)


if __name__ == '__main__':
    main()
