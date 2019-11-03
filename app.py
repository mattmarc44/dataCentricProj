import os
from flask import Flask, redirect, render_template, url_for, request, session, jsonify
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import math

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
    limit = int(request.args.get('limit', 6))
    offset = int(request.args.get('offset', 0))
    page_num = int(request.args.get('page_num', 1))
    jump = int(request.args.get('jump', 1))

    #set defaults to avoid bad url's being made
    if limit < 1:
        limit = 5
    if offset < 0:
        offset = 0
    if page_num < 1:
        page_num = 1

    starting_id = mongo.db.movies.find().sort('_id', pymongo.ASCENDING)
    last_id = starting_id[offset]['_id']

    movies = mongo.db.movies.find({'_id': {'$gte': last_id}}).sort('_id', pymongo.ASCENDING).limit(limit)
    entries = mongo.db.movies.find().count()
    length_float = float(entries) / float(limit)
    length = int(math.ceil(length_float))

    output = []
    for i in movies:
        try:
            output.append({
                '_id': i['_id'],
                'movie_name': i['movie_name'],
                'genre': i['genre'],
                'short_description': i['short_description'],
                'release_date': i['release_date'],
                'rating': i['rating'],
                'director': i['director'],
                'run_time': i['run_time'],
                'full_description': i['full_description'],
                'picture': i['picture']
                })
        except:
            output.append({
                '_id': i['_id'],
                'movie_name': i['movie_name'],
                'genre': i['genre'],
                'short_description': i['short_description'],
                'release_date': i['release_date'],
                'rating': i['rating'],
                'director': i['director'],
                'run_time': i['run_time'],
                'full_description': i['full_description']
                })
                

    next_url = '/?limit=' + str(limit) + '&offset=' + str(offset + limit) + '&page_num=' + str(page_num + 1)
    prev_url = '/?limit=' + str(limit) + '&offset=' + str(offset - limit) + '&page_num=' + str(page_num - 1)
    current_url = '/?limit=' + str(limit) + '&offset=' + str(offset) + '&page_num=' + str(page_num)
    # incomplete logic for jumping multiple pages, need to find a way to get amount of pages to jump relative
    # to the page the client is on. for ex. if on page 3 and clicks on one, how to get that 2 jump var
    page_up_url = '/?limit=' + str(limit) + '&offset=' + str(offset + (limit*jump)) + '&page_num=' + str(page_num + jump)
    page_down_url = '/?limit=' + str(limit) + '&offset=' + str(offset - (limit*jump)) + '&page_num=' + str(page_num - jump)


    result = {'result': output, 'next_url': next_url, 'prev_url': prev_url, 'current_url': current_url, 'page_up_url': page_up_url, 'page_down_url': page_down_url}
    return render_template('index.html', movies=result, length=length, page_num=page_num, page_title='Home')


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
    return render_template('edit_movie.html', movie=selected_movie, genres=genre_list, page_title='Edit Movie')

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
#deletes a movie depending on the movie page you are on
def delete_movie(movie_id):
    mongo.db.movies.remove({'_id': ObjectId(movie_id)})
    return redirect(url_for('get_movies'))

@app.route('/movie_page/<movie_id>')
#returns a page specific for a chosen movie
def movie_page(movie_id):
    selected_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movie_page.html', movie=selected_movie, page_title='Movie Page')


#GENRE
#search by genre 
@app.route('/get_genres')
#gets genre list
def get_genres():
    return render_template('genres.html', genres=mongo.db.genres.find(), page_title='Genres')

@app.route('/search/<search_id>')
#get page of films filtered by a selection
def genre_search(search_id):
    selected = mongo.db.movies.find({"genre": search_id})
    return render_template('search_result.html', movies=selected, query=search_id, page_title='Search Results')


#SEARCH QUERY
@app.route('/title_search', methods=['GET'])
#searches for a query amongst titles
def title_search():
    query = request.args.get('search')
    searched = mongo.db.movies.find({'movie_name': query})
    return render_template('search_result.html', movies=searched, query=query, page_title='Search Results')

app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)