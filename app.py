import os
from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run()
