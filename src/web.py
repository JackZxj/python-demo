import asyncio
import threading
import time
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates',
            static_folder='static', static_url_path='/')
x = []

@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/values')
def get_values():
    return 'null'


if __name__ == '__main__':
    app.run()
