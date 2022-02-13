import os
from pydoc import describe
from wiki import getwikiurl
import random

from flask import Flask, render_template
from tmdb import get_movie_data


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello():
    
    listofmovies = ['634649', '447332', '122', '603', '272', '6479', '1402']
    movie = random.choice(listofmovies)
    movie_data = get_movie_data(movie)
    wikititle = movie_data['name']
    wiki_data = getwikiurl(wikititle)
    return render_template(
        'index.html',
        name = movie_data['name'],
        description = movie_data['description'],
        genres = movie_data['genres'],
        poster = movie_data['poster'],
        wikilink = wiki_data['wiki']
        )
    

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)