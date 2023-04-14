import requests
from dotenv import dotenv_values
import os
import api_token
from random import shuffle

# Nie udało się wykorzystać metody ze zmiennymi środowiskowymi, zamiast tego używam funkcji która po prostu zwraca token i jest w pliku oznaczonym w gitignore
API_token = api_token.get_api_token()

list_of_types = ["popular", "upcoming", "top_rated", "now_playing"]


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    params = {
        "api_key": API_token,
    }
    response = requests.get(full_url, params=params)
    return response.json()


def get_movies_list(list_name="popular"):
    return call_tmdb_api(f"movie/{list_name}")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_name="popular"):
    data = get_movies_list(list_name)
    shuffle(data["results"])
    return data["results"][:how_many]


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]
