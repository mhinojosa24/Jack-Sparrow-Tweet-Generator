from flask import Flask
from stochastic_sampling import *

app = Flask(__name__)

@app.route('/')
def generate_sentence():
    file = 'sample_corpus.txt'
    random_words = randomized_word(file)
    return random_words
