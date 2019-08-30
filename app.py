import os
from flask import Flask, redirect, render_template, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

app.config["MONGO_DBNAME"] = 'movie_reviews'
app.config["MONGO_URI"] = 'mongodb+srv://' + db_user + ':' + db_pass + '@clustertitmuss-8wiik.mongodb.net/movie_reviews?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_movies')
def get_movies():
    return render_template('index.html', movies=mongo.db.movies.find(), page_title='Home')


app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)