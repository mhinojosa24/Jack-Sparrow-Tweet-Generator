
import random, sys
from histogram import *
'''
<-- Functions -->

randomized_word()
    - takes a 'source_text' argument.
    - stores a text file in a listogram
    - returns a word based on its frequency

test_word()
    - calculates the total amount of each word based on it's frequency
    
'''

list = 'one fish two fish red fish blue fish'

def randomized_word(histogram):
    total_count = 0 #find what this value is
    chance = 0.0 #'chance' is the probability of getting a particular word
    listogram = list_of_list(histogram) #list of list of unique words and its frequency
    random_num = random.random() #random number from 0 & 1

'''loops through listogram & add the total count of each word'''
    for word_list in listogram:
        total_count += word_list[1]

    for word_set in listogram:
        chance += word_set[1] / total_count #divide the words frequency with total count
        if chance >= random_num: #check the chance of getting a particular based on their probability
            return word_set[0]


def test_word():
    source = sys.argv[1]
    test = {}

    for i in range(10000):
        random_word = randomized_word(source)
        if random_word not in test:
            test[random_word] = 1

        else:
            test[random_word] += 1

    return test



if __name__ == "__main__":
    print(test_word())
