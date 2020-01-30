import random


def dictionary_words(number=1):
    my_file = open("/usr/share/dict/words", "r")
    lines = my_file.read().splitlines()
    word_list = []
    for _ in range(number):
        random_index = random.randint(0, len(lines) - 1)
        word_list.append(lines[random_index])
    return word_list

if __name__ == '__main__':
    sentence = dictionary_words(5)
    print(sentence)

    

