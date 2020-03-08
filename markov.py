from dictogram import Dictogram

class MarkovChain:

    def __init__(self, word_list):
        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0] 

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):        
        first_word = random.choice(list(self.word_dict.keys())) 
        sentence = []
        print(self.word_dict)
        print("first_word", first_word)
        for i in range(count):
            second_word = self.word_dict[first_word]
            next_word = second_word.sample()
            first_word = next_word
            sentence.append(next_word)
            
        end_words = []
        for index in range(len(self.token)-1):
            if len(self.word_dict[self.token[index]]) == 1:
                end_words.append(self.token[index])
        last_word = random.choice(end_words)
        sentence.append(last_word)
        sentence = ' '.join(sentence)
        sentence = sentence.capitalize()
        return sentence + "."

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))