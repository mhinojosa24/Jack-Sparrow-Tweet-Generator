# from nltk.corpus import words
from stochastic_sampling import *
from dictogram import Dictogram
import random




def markov_chain(list_of_values):
    mc = Dictogram()

    i = 0
    while i < len(list_of_values) - 2:
        pair = (list_of_values[i], list_of_values[i+1]) # pair of words in tuple
        next_word = list_of_values[i+2] # next word
        if pair in mc: # check to see if pair of words exist in the dictionary
            mc[pair].add_count(next_word) # increments the count of the next word

        else:
            new_dict = Dictogram() # new dictionary
            new_dict.add_count(next_word) # add count of next word
            mc[pair] = new_dict #
        i += 1
    print('markov chain ==> \n', mc, '\n<== end of markov chain\n')
    return mc


def generate_sentence(dictogram, num_words):
    all_keys = []
    words_for_sent = []
    new_sentence = ''

    for i in range(num_words):
        for index, keys in enumerate(dictogram):
            all_keys.append(keys)

        random_set = random.choice(all_keys) # <== gets random choice from all key pair of words
        # print('random tuple set ==> ', random_set, '\n<== end of random tuple set \n')

        words_for_sent.append(random_set[0])
        words_for_sent.append(random_set[1])

        get_next_set = dictogram[random_set]
        # print("next set of tuple ===> ", get_next_set)
    print('words for sentence ==> ', words_for_sent, '\n<== end\n')

    for word in words_for_sent:
        new_sentence += word + " "
    return new_sentence









    # for i in range(num_words):
    #     tuple_key =  tuple(words_for_sent[-2:])
    #
    #     value = dictogram[tuple_key]
    #     sampler_word = randomized_word(value)
    #     words_for_sent.append(sampler_word)
    #
    #
    #     for word in  words_for_sent:
    #
    #         new_sentence += word + " "
    #
    # return new_sentence
    #


def main():
    sample = 'I like cats. I love dogs. I hate nasty food. Although I love love food.'
    sample = sample.split(" ")
    dict = markov_chain(sample)
    # print(dict)
    gen = generate_sentence(dict, 10)
    print(gen)


if __name__ == '__main__':
    main()
