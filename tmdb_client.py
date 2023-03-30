import requests
from dotenv import dotenv_values
import os
import api_token
from random import shuffle

# Nie udało się wykorzystać metody ze zmiennymi środowiskowymi, zamiast tego używam funkcji która po prostu zwraca token i jest w pliku oznaczonym w gitignore
API_token = api_token.get_api_token()


def get_movies_list(list_name="popular"):
    # Zakomentowany kod niestety nie działa i nie znalazłem rozwiązania.
    # endpoint = "https://api.themoviedb.org/3/movie/popular"
    # headers = {"Authorization": f"Bearer {API_token}"}
    # response = requests.get(endpoint, headers=headers)
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}?api_key={API_token}"
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_name="popular"):
    data = get_movies_list(list_name)
    shuffle(data["results"])
    print(data)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_token}"
    response = requests.get(endpoint)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = (
        f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_token}"
    )
    response = requests.get(endpoint)
    return response.json()["cast"]
