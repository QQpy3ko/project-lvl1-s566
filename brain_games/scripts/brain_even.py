#!/usr/bin/env python3

from brain_games import game_engine
from brain_games.games import brain_even


def main():
    game_engine.run_game(brain_even)


if __name__ == '__main__':
    main()
