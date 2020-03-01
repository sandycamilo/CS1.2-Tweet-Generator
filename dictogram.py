from random import randint

class Dictogram:

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        self.word_list = word_list #Text file converted into word list
        
        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values()) # number of all the words in the dictionary
        self.types = self.unique_words() #self.types is assigned to the unique.words function

    def build_dictogram(self): 
        '''Creates a histogram dictionary using the word_list property and returns it'''
        #TODO: use your histogram function as a starting point to complete this method
        hist_dict = {} #creates dictionary called hist_dict
        for words in self.word_list: # for loop - for every word in the list called word_list that has a .self in front indicating its association with the class Dictogram
            if words in hist_dict.keys(): # if word is in the dictionary stored in the keys of the key, value pairs
                hist_dict[words] += 1 # add one to the value of the word in the dictionary
            else:
                hist_dict[words] = 1 # the count of the word stays as it is with a value of one- one because we know it exists 
        return hist_dict  

    def frequency(self, word):
        '''returns the frequency or count of the GIVEN word in the dictionary histogram'''
        #TODO: use your frequency function as a starting point to complete this method
        return self.dictionary_histogram[word]

    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        return len(self.dictionary_histogram.keys()) #len returns the number of items is the dictionary_histogram by accessing it with the keys funciton

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''
        #TODO: use your sample function as a starting point to complete this method 
        word = randint(0, len(self.dictionary_histogram) -1) # random word from the histogram
        end = 0 #counter 
        for key, value in self.dictionary_histogram.items(): # for every key and value in histogram
            end += value # counter is equal to the current value of the counter plus value of the key
            if end >= word: # if counter is more or equal to than the value of the word
                return key 
        

def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    # print_dictogram_samples(dictogram)

def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])