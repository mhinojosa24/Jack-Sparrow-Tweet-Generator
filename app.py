from flask import Flask, render_template
# # from stochastic_sampling import *
#
# import sys
app = Flask(__name__)
#
#
@app.route('/')
def main():
    return 'hi'
    # return generate_sentence()
    # return render_template('index.html')

#tempo comment
def generate_sentence():
    file = 'sample_corpus.txt'
    random_words = randomized_word(file)
    return random_words
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Worlddd!'
