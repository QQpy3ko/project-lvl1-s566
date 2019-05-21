from brain_games import cli
from brain_games.scripts.chanks import even_session


def main():
    print("Welcome to the Brain Games!")
    print('Answer "yes" if number even otherwise answer "no".')

    cli.run()

    even_session.run_game()


if __name__ == '__main__':
    main()
