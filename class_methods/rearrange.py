import random


def reorganize_quote(sentence):
    array = sentence.split(' ')
    new_array = []

    '''
    checks each word if it contains ".", if so, remove the "." from word.
    then randomly inserts each word in a different index.
    '''
    for word in array:
        rand_int = random.randint(0, len(array))

        if "." in word:
            word = word[:-1] # removes the last character of index
            # reversed_word = word[::-1] # reverse word
            new_array.insert(rand_int, word)
        else:
            # reversed_word = word[::-1]
            new_array.insert(rand_int, word)

    sentence = ' '.join(new_array) + "."



    new_sentence = sentence[:1].upper() + sentence[1:]

    return new_sentence

def main():
    user_input = input("Please enter a sentece to rearrange: ")
    print(reorganize_quote(user_input))

if __name__ == "__main__":
    main()
