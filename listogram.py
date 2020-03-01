from random import randint

class Listogram:

    def __init__(self, word_list):
        '''Initializes the listogram properties'''
        self.word_list = word_list
        self.list_histogram = self.build_listogram()
        self.tokens = self.get_num_tokens()
        self.types = self.unique_words()

    def build_listogram(self): 
        '''Creates a histogram list of lists using the word_list property and returns it'''
        #TODO: use your listogram function as a starting point to complete this method
        histogram_list = [] #creates a list called histogram_list
        for word in self.word_list: # for every word in the word list 
            index = self.get_index(word, histogram_list) # index holds the value of the index of the word in the new created list 
            if index == 'did not find it': # word is not there 
                histogram_list.append([word, 1]) # append the word to the list-  with the value of one 
            else:
                innerlist = histogram_list[index] #accessing the inner list with the index
                innerlist[1] += 1 #adding one to the count 
        return(histogram_list)

    def get_num_tokens(self):
        '''gets the number of tokens in the listogram'''
        tokens = 0 #tokens is set to a value of zero
        for item in self.list_histogram: # for every item in the list histogram 
            tokens += item[1] # tokens with the value of zero is increased by the value of the item that has a default value of one 
        return tokens # the value of tokens is returned

    def get_index(self, word, list_histogram):
        '''searches in the list histogram parameter and returns the index of the inner list that contains the word if present'''
        #TODO: use your get_index function as a starting point to complete this method
        index = 0
        for innerlist in list_histogram: # for every list word in list histogram
            #index = word.index(list_word) # created a new variable called index where the index of the list word is stored of the 
            #return index
            if word == innerlist[0]:
                return index
            index += 1 
        return 'did not find it'


    def frequency(self, word):
        '''returns the frequency or count of the given word in the list of lists histogram'''
        #TODO: use your frequency and get_index function as a starting point to complete this method
        #You will need to adapt it a little bit to work with listogram
        for index in range(len(self.list_histogram)): # getting index from list histrogram
            if self.list_histogram[index][0] == word: # if word in list histogram matches the word 
                return self.list_histogram[index][1] # return the count of the word
            return 0 # otherwise return 0
        
    def unique_words(self):
        '''returns the number of unique words in the list of lists histogram'''
        #TODO: use your unique words function as a starting point to complete this method
        #You will need to adapt it a little bit to work with listogram
        return len(self.list_histogram) # returns the number of the length of all the items in the list histogram


    def sample(self):
        '''Randomly samples from the list of list histogram based on the frequency, returns a word'''
        #TODO: use your sample function as a starting point to complete this method 
        #You will need to adapt it a little bit to work with listogram
        # one fish two fish blue fish red fish 
        # [['fish', 4], ['one', 1], ['two', 1], ['red', 1], ['blue', 1]]
        word = randint(0, len(self.list_histogram) -1) # random word from the list histogram
        end = 0 #counter
        for key, value in self.list_histogram: # if the item in the list histogram's items
            end += value 
            if end >= word:
                return key 

def print_listogram(word_list):
    '''Creates a list based histogram (listogram) and then prints out its properties and samples from it'''

    print()
    print('List of Lists Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    listogram = Listogram(word_list)
    print('listogram: {}'.format(listogram.list_histogram))
    print('{} tokens, {} types'.format(listogram.tokens, listogram.types))
    for word in word_list[-2:]:
        freq = listogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    # print_dictogram_samples(listogram)

def print_dictogram_samples(listogram):
    '''Compares sampled frequency to observed frequency'''

    print('List of Lists Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [listogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist.list_histogram))
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
    for item in listogram.list_histogram:
        word = item[0]
        count = item[1]
        # Calculate word's observed frequency
        observed_freq = count / listogram.tokens
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

print_listogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])