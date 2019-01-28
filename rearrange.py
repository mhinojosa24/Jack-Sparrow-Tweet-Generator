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
        print(rand_int)
        if "." in word:
            word = word[:-1] # removes the last character of index
            reversed_word = word[::-1] # reverse word
            new_array.insert(rand_int, reversed_word)
        else:
            reversed_word = word[::-1]
            new_array.insert(rand_int, reversed_word)

    new_array = ' '.join(new_array) + "."
    new_array = new_array[:1].upper() + new_array[1:]

    return new_array

# reorganize_quote("max")
def main():
    user_input = input("Please enter a sentece to rearrange: ")
    print(reorganize_quote(user_input))

if __name__ == "__main__":
    main()
