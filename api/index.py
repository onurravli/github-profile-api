from flask import Flask

app = Flask(__name__)


def api_usage():
    print('''
    Usage:
        python index.py
    ''')


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About'
