from webbrowser import get
import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/movie"
API_KEY = os.getenv("API_KEY")
#movid = 'tt6644200'

def get_movie_data(movid):
    params = {
        "api_key": API_KEY,
        "movie_id": movid
    }

    response = requests.get(
        f'{BASE_URL}/{movid}',
        params=params,
    )

   

    def get_name(movies):
        return response.json()['original_title']

    def get_description(movies):
        return response.json()['tagline']

    def get_generes(movies):
        mystring = ''
        gen = response.json()['genres']
        list = []
        for single in gen:
            seperator = ', '
            list.append(single['name'])
            x = seperator.join(list)
        return x

    def get_poster(movies):
        return response.json()['poster_path']

    ot = get_name(response)
    description = get_description(response)
    genres = get_generes(response)
    poster_path = get_poster(response)

    return {
        'name': ot,
        'description': description,
        'genres': genres,
        'poster': poster_path
    }
