import sys as sys
import random

def rearrange_words():
    args = sys.argv[1:]
    random_index = random.randint(0, len(args) -1)
    return args[random_index]


if __name__ == "__main__":
    words = rearrange_words()
    print(words)
  