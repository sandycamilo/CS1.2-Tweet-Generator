import sys as sys
from random import randint

if __name__ == "__main__":
    args = sys.argv[1:]

    random_index = randint(0, len(args) -1)
    print(args[random_index])