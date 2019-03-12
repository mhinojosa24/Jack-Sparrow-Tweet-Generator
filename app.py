from flask import Flask, render_template
from markov_chain import *
from flask import render_template



app = Flask(__name__, template_folder='templates', static_folder='css')



with open('text_file.txt', "r") as f:
    data = f.read().decode("utf-8", "replace")
    words_list = data.split()


@app.route('/')
def generator():
    markov = markov_chain(words_list)
    sentence = generate_sentence(markov, 10)
    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True) #
