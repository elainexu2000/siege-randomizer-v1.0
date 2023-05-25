import sys
from flask import Flask, redirect, render_template, request, url_for
sys.path.append("../")
from siege_randomizer import get_random_operator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    generated_string = get_random_operator().get_random_loadout()
    return generated_string

if __name__ == '__main__':
    app.run()
