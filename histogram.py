
def histogram(story):
    """Returns dictionary of key-value pairs"""
    # return data structure that stores each unique word 
    # and number of times the word appears on story
    print(story)
    # {'one':1, 'two':1, 'red':1, 'blue':1, 'fish':4}
    # one fish two fish red fish blue fish
    hist_dict = {}
    story_lines = story.split() #turns string into a list 
    for words in story_lines: #iterating through every word in story_lines
        if words in hist_dict.keys(): # if the word was already in the histogram  ~ .keys returns all keys in the dictionary
            hist_dict[words] += 1 #increasing the frequency by one 
        else:
            hist_dict[words] = 1 #initializing the word with frequency of 1 - only sees it once so it is equal to one
    return hist_dict

def unique_words(histogram):
    return len(histogram.keys()) #.keys accessed the histogram to count every key and len is the method that gives me the total count of the items on the list  ~ counts ALL words 

def frequency(word, histogram):
    return histogram[word]  #gives me the frequency of one word the word that i pass it on 
 
if __name__ == '__main__':
    story = open("source_text.txt", "r")
    lines = story.read()
    # print(lines)
    for line in lines:
        pass
        # print(line)
    hist = histogram(lines)
    word = 'together'
    print(unique_words(hist))
    print(frequency(word, hist))
    print(hist)
    
    
    
    