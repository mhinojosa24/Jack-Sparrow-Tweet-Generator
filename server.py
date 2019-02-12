from flask import Flask, render_template
from stochastic_sampling import *

import sys
app = Flask(__name__)


@app.route('/')
def main():
    return generate_sentence()
    # return render_template('index.html')


def generate_sentence():
    file = 'sample_corpus.txt'
    random_words = randomized_word(file)
    return random_words
