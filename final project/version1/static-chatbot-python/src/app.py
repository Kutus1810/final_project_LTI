from flask import Flask, request, jsonify, render_template
import pandas as pd
from chatbot import get_commands

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('query')
    commands = get_commands(user_input)
    return jsonify(commands)

if __name__ == '__main__':
    app.run(debug=True)