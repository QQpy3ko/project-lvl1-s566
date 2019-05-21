import operator
import random
from brain_games.scripts import game_template


def main():
    game_template.greeting()

    print('What is the result of the expression?')
    
    game_template.ask_name()

    operators = {
        '+': operator.add, 
        '-': operator.sub,
        '*': operator.mul
    }


    def set_question_and_answer(question, correct_answer):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        random_operator_key = random.choice(list(operators))
        question = str(a) + '' + random_operator_key + '' + str(b)    
        correct_answer = str(operators[random_operator_key](a, b))
        return question, correct_answer

    game_template.run_game(set_question_and_answer)


if __name__ == '__main__':
    main()