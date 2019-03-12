import re


def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text

def split_on_whitespaces(text):
    return re.split('\s+', text)


def tokenize(text_list):
    text = ' '.join(text_list)
    no_punc_text = remove_punctuation(text)
    tokens = split_on_whitespaces(no_punc_text)
    return tokens


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        # print(source)
        tokens = tokenize(source)
        print(tokens)

    else:
        print('No source text filename give as argument')
