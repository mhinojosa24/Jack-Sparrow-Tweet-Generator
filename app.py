from flask import Flask, render_template, request, redirect
from flask import request
from markov_chain import *
import sys
# import twitter



app = Flask(__name__, template_folder='templates', static_folder='css')



with open('text_file.txt', "r") as f:
    data = f.read()
    data = data.decode("utf-8", "replace")
    words_list = data.split()


@app.route('/')
def generator():
    markov = markov_chain(words_list)
    sentence = generate_sentence(markov, 10)
    return render_template('index.html', sentence=sentence)

# @app.route('/tweet', methods=['POST'])
# def tweet():
#     status = request.form['sentence']
#     twitter.tweet(status)
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
