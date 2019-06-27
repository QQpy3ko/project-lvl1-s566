#!/usr/bin/env python3

from brain_games import cli
from brain_games import game_engine


def main():
    game_engine.greet()
    cli.ask_name()


if __name__ == '__main__':
    main()
