import random, sys
from histogram import *

'''
<-- Functions -->

histogram()
    - takes a 'source_text' argument and return a histogram data structure that stores each unique word.

'''

list = 'one fish two fish red fish blue fish'

def probability(histogram):
    # tokens = total count of words
    tokens = 0 # find what this value is
    listogram = list_of_list(histogram)
    updated_array = []
    counter = 10000

    while counter > 0:
        counter -= 1
        for word_list in listogram:
            tokens += word_list[1]

    for small_list in listogram:
        updated_array.append([small_list[0], small_list[1] / tokens])
    print(updated_array)



    # result = '{}: {}'.format(word, tokens)
    # print('Tokens: {}'.format(tokens))
    # return(result)

    # make a new list that looks something like:
     #[['one', 0.125], ['fish', 0.5], ['two', 0.125], ['red', 0.125], ['blue', 0.125]]


probability(list)
