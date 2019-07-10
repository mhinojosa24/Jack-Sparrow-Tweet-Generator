from flask import Flask, render_template, request, redirect
from flask import request
from markov_chain import *
from cleanup import cleanup
from tokenized import tokenize
import sys
import twitter


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def generator():
    source_text = 'corpus.txt'
    clean_text = cleanup(source_text)
    tokenize_text = tokenize(clean_text)
    markov = markov_chain(tokenize_text)
    sentence = generate_sentence(markov, 4)
    return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
