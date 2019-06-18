 #!/usr/bin/env python3

from brain_games.scripts import cli
from brain_games.games import game_engine


def main():
    game_engine.greeting()
    cli.run()


if __name__ == '__main__':
    main()
