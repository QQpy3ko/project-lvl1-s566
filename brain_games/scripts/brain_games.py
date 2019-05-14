import sys 
sys.path.append('..') # to be able import from parent

from cli import run


def main():
    print("Welcome to the Brain Games!")

    run()

if __name__ == '__main__':
	main()