from nltk.corpus import words
from stochastic_sampling import *
from dictogram import Dictogram




def generate_dict(sample):
    new_dict = {}
    sentences = sample.split('.')
    start = '🏳️'
    stop = '🏁'
    new_dict[start] = Dictogram()
    new_dict[stop] = Dictogram()


    for sentence in sentences:
        words = sentence.split(' ')
        if words[0] == '':
            del words[0]
        else:
            print('####', new_dict[start])
            new_dict[start].add_count(words[0])
            print('####', new_dict[stop])
            new_dict[stop].add_count(words[len(words) - 1])
            print(new_dict)
        # return
        for _ in range(1, len(words) -1):
            if words in new_dict:
                new_dict[word] = Dictogram()
                print(new_dict)

def main():
    sample = 'I like cats. I love dogs. I hate nasty food.'
    dict = generate_dict(sample)
    print(dict)


if __name__ == '__main__':
    main()
