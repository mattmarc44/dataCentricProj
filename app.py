import os
from flask import Flask, redirect, render_template, url_for, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page_title='Home')


app.run(host=os.getenv('IP', "0.0.0.0"), port=os.getenv('PORT', "5000"), debug=False)