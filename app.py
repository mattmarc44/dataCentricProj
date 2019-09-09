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
#Gets a list of movies and returns them on the homepage
def get_movies():
    return render_template('index.html', movies=mongo.db.movies.find(), page_title='Home')

@app.route('/add_movie')
#returns the page with a form for adding a film to the database
def add_movie():
    return render_template('add_movie.html', genres=mongo.db.genres.find(), page_title='Add Movie')

@app.route('/insert_movie', methods=['POST'])
#the route  for form submission on add_movie
def insert_movie():
    mongo.db.movies.insert_one(request.form.to_dict())
    return redirect(url_for('get_movies'))

@app.route('/edit_movie/<movie_id>')
#returns a page to edit an existing movie
def edit_movie(movie_id):
    selected_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    all_genres = mongo.db.genres.find()
    genre_list = [genre for genre in all_genres]
    return render_template('edit_movie.html', movie=selected_movie, genres=genre_list)

@app.route('/update_movie/<movie_id>', methods=['POST'])
#the route  for form submission on edit_movie
def update_movie(movie_id):
    mongo.db.movies.update( {'_id': ObjectId(movie_id)},
    {
        'movie_name': request.form.get('movie_name'),
        'genre': request.form.get('genre'),
        'short_description': request.form.get('short_description'),
        'release_date': request.form.get('release_date'),
        'rating': request.form.get('rating'),
        'director': request.form.get('director'),
        'run_time': request.form.get('run_time'),
        'full_description': request.form.get('full_description')
    })
    return redirect(url_for('get_movies'))

@app.route('/delete_movie/<movie_id>')
def delete_movie(movie_id):
    mongo.db.movies.remove({'_id': ObjectId(movie_id)})
    return redirect(url_for('get_movies'))

@app.route('/movie_page/<movie_id>')
#returns a page specific for a chosen movie
def movie_page(movie_id):
    selected_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movie_page.html', movie=selected_movie)

app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)