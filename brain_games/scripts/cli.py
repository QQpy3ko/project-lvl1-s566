 #!/usr/bin/env python3

import prompt


# name = [] # road to hell, used var = return of function 'run'


def run():

    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
