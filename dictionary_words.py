from rearrange import reorganize_quote
from nltk.corpus import words
import random
import sys

'''
- read in the words file
- select a random set of words from the file and store in a data type
- put the number of words requested together into a "sentence"
- output your senence

'''



def set_of_words(number_of_words):
    file_name = "/usr/share/dict/words"

    random_words = []
    word_count = 0

    # file = open(file_name, "w")
    # file.write(words_to_string)
    # file.close()


    with open( "/usr/share/dict/words", "r") as f:
        data = f.read()
        words_list = data.split() #puts words object into an array of strings


    while word_count != number_of_words:
        random_int = random.randint(0, len(words_list)) #random number to get a random index for list of words

        random_word = words_list[random_int] #gets a random word from list of words
        random_words.append(random_word) #appends random word in the list of random words
        word_count += 1 #counts the number of random words to meet a break point

    return make_sentence(random_words)


def make_sentence(list_of_words):

    sentence = ' '.join(list_of_words) + "."
    capitalized_sentence = sentence[:1].upper() + sentence[1:]

    return capitalized_sentence

def main():

    num_provided = False
    while not num_provided:
        # user_input = input("How many words would you like? ")
        try:
            # number = int(user_input)
            number = int(sys.argv[1]) # user input data
            print(set_of_words(number))
            num_provided = True

        except ValueError:
            print("Oops! Please enter a integer (: ")


if __name__ == "__main__":
    main()
