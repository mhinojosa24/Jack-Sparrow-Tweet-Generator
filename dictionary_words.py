from rearrange import reorganize_quote
from nltk.corpus import words
import random

'''
- read in the words file
- select a random set of words from the file and store in a data type
- put the number of words requested together into a "sentence"
- output your senence

'''

words = words.words() #words are in a array

words_to_string = ''.join(words)
random_words = []


def set_of_words(number_of_words):
    file_name = "words.txt"
    file = open(file_name, "w")
    file.write(words_to_string)
    file.close()

    word_count = 0

    with open(file_name, "r") as f:
        file_data = f.readlines()

        for data in file_data:
            word_count += 1
            word = data.split()

        for word in range(number_of_words):
            if len(random_words) != number_of_words:
                random_int = random.randint(0, len(words) -1) #returns a random index integer
                random_word = words[random_int] #returns a random word
                random_words.append(random_word)
                string_of_words = ' '.join(random_words)
        print(string_of_words)

set_of_words(10)

def main():
    user_input = int(input("How many words would you like?"))

    set_of_words(user_input)



if __name__ == "__main__":
    main()
