import sys
from flask import Flask, redirect, render_template, request, url_for
sys.path.append("../")
from siege_randomizer import get_random_operator, get_random_attacker, get_random_defender

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_attacker')
def generate_attacker():
    generated_string = get_random_attacker().get_random_loadout()
    return generated_string

@app.route('/generate_defender')
def generate_defender():
    generated_string = get_random_defender().get_random_loadout()
    return generated_string

@app.route('/generate_all')
def generate_all():
    generated_string = get_random_operator().get_random_loadout()
    return generated_string

if __name__ == '__main__':
    app.run()
