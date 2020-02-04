import sys as sys
import random

def rearrange_words(number=1):
    args = sys.argv[1:]
    for _ in range(number):
        random_index = random.randint(0, len(args) -1)
        args.append(args[random_index])
    return args

if __name__ == "__main__":
    words = rearrange_words()
    print(words)
  