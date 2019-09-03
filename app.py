import os
from flask import Flask, redirect, render_template, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

app.config["MONGO_DBNAME"] = 'movie_reviews'
app.config["MONGO_URI"] = 'mongodb+srv://{}:{}@clustertitmuss-8wiik.mongodb.net/movie_reviews?retryWrites=true&w=majority'.format(db_user, db_pass)

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_movies')
def get_movies():
    return render_template('index.html', movies=mongo.db.movies.find(), page_title='Home')

@app.route('/add_movie')
def add_movie():
    return render_template('add_movie.html', genres=mongo.db.genres.find(), page_title='Add Movie')

@app.route('/insert_movie', methods=['POST'])
def insert_movie():
    mongo.db.movies.insert_one(request.form.to_dict())
    return redirect(url_for('get_movies'))

@app.route('/movie_page/<movie_id>')
def movie_page(movie_id):
    selected_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    # all_genres = mongo.db.genres.find()
    return render_template('movie_page.html', movie=selected_movie)

app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)