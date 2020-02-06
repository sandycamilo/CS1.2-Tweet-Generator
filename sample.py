import random
from histogram import histogram , frequency
             
# def sample_by_frequency(histogram):
#   word = random.randint(0, len(histogram) -1)
#   lines = []
#   for key, value in histogram.items():
#     lines.append( key * value )
#   return lines

def sample_by_frequency(histogram):
    word = random.randint(0, len(histogram) -1)
    end = 0
    for key, value in histogram.items():
        end += value 
        if end >= word:
            return key

    # word = random.randint(0, histogram)
    # print(word)
    # lines = []
    # for key, value in histogram.items():
    # print(key, value)
        # for _ in range(value):
        #     lines.append(key) 
    # print(lines[word])
    # return lines

if __name__ == "__main__":
    pass
