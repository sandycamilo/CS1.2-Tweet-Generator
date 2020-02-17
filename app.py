from flask import Flask 
from histogram import histogram #imports histogram function from histogram file
from sample import sample_by_frequency

app = Flask(__name__)

@app.route('/')
def generate_words():
    #build a histogram
    my_file = open("./source_text.txt", "r")  # opens file and reads it 
    lines = my_file.readlines() # makes a string of all lines in file and stores it in 'lines'
    my_histogram = histogram(lines) 

    ### generate a sentence 
    sentence = " "
    num_words = 10 
    for i in range(num_words):
        word = sample_by_frequency(my_histogram)
        sentence += " " + word
    return sentence

    
    word = sample_by_frequency(my_histogram)
    return word

if __name__ == "__main__":
    pass