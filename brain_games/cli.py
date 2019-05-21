import prompt


inputed_name = []
# the task ('put input-logic in function run') screwed me to this way


def run():
    inputed_name.append(prompt.string('May I have your name? '))
    print(f"Hello, " + inputed_name[0] + '!')