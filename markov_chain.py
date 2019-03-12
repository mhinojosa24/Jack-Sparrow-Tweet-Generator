# from nltk.corpus import words
# from class_methods.stochastic_sampling import *
from stochastic_sampling import *
# from class_methods.dictogram import Dictogram
from dictogram import Dictogram
import random, re




def markov_chain(list_of_values):
    mc = Dictogram()

    i = 0
    while i < len(list_of_values) - 3:
        pair = (list_of_values[i], list_of_values[i+1], list_of_values[i+2]) # pair of words in tuple
        # print(list_of_values[i], list_of_values[i+1], list_of_values[i+2], list_of_values[i+3], list_of_values[i+5])
        next_word = list_of_values[i+3] # next word

        if pair in mc: # check to see if pair of words exist in the dictionary
            mc[pair].add_count(next_word) # increments the count of the next word

        else:
            new_dict = Dictogram() # new dictionary
            new_dict.add_count(next_word) # add count of next word
            mc[pair] = new_dict #
        i += 1
    # print('markov chain ==> \n', mc, '\n<== end of markov chain\n')
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
        if random_set is not None:
            words_for_sent.append(random_set[0])
            words_for_sent.append(random_set[1])
            words_for_sent.append(random_set[2])
            

            get_next_set = dictogram[random_set]
        # print('next set of tuple ===> ', get_next_set)
    # print('words for sentence ==> ', words_for_sent, '\n<== end\n')

    for word in words_for_sent:
        new_sentence += word + " "
    return new_sentence



def main():
    sample = 'I like cats. I love dogs. I hate mr.max nasty food. Although I love love food.'
    with open( 'corpus.txt', "r") as f:
        data = f.read()
        # words_list = data.split()
        content = re.sub('[^a-zA-Z0-9 \n\.]', '', data)
        sample = data.split(' ')
        dict = markov_chain(sample)
        # print(dict)
        gen = generate_sentence(dict, 4)
        return gen


if __name__ == '__main__':
    main()
