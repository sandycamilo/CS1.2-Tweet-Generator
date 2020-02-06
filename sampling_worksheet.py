import random

histogram = [('cats', 3), ('dogs', 4), ('rabbits', 2), ('turtles', 1)]

def sample(histogram):
    tokens = sum([count for word, count in histogram]) 
    dart = random.randint(1, tokens) 
    fence = 0 

    for word, count in histogram:
        fence += count 
        if fence >= dart:  
            return word

print(sample(histogram))
