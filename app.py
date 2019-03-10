from flask import Flask, render_template
from markov_chain import *
app = Flask(__name__)

@app.route('/')
def generator():
    with open( 'text_file.txt', "r") as f:
        data = f.read()
        words_list = data.split()
    mc = markov_chain(words_list)
    sentence = generate_sentence(mc, 10)
    return sentence
