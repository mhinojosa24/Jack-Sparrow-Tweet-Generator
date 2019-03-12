

def cleanup(source_text):
    '''This method cleans the text document'''

    with open(source_text, 'r') as f:
        text_body = f.read().decode('utf-8', 'replace')

    removed_new_lines = text_body.replace('\n', '')
    removed_commas = removed_new_lines.replace(',', ' ')
    removed_periods = removed_commas.replace('.', ' ')
    pruned_source_text = removed_periods.split(' ')

    for index in range(len(pruned_source_text)):
        word = pruned_source_text[index].lower()
        pruned_source_text[index] = word

    for word in pruned_source_text:
        if word == '':
            pruned_source_text.remove(word)

    return pruned_source_text

if __name__ == '__main__':
    file = 'corpus.txt'
    text = cleanup(file)
    print(text)
