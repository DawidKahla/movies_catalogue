import tmdb_client
from unittest.mock import Mock


def test_get_movies_list(monkeypatch):
    mock_movies_list = ["Movie 1", "Movie 2"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movies_list(list_name="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    mock_movie = "Movie 1"
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movie = tmdb_client.get_single_movie(1)
    assert movie == mock_movie


def test_get_poster_url():
    poster_api_path = "poster_path"
    default_size = "w342"
    base_url = "https://image.tmdb.org/t/p/"
    expected_url = f"{base_url}{default_size}/{poster_api_path}"
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_url == poster_url


def test_get_single_movie_cast(monkeypatch):
    mock_cast = ["Credit 1", "Credit 2"]
    requests_mock = Mock()
    response_mock = Mock()
    response_mock.json.return_value = {"cast": mock_cast}
    requests_mock.get.return_value = response_mock
    monkeypatch.setattr("tmdb_client.requests", requests_mock)
    cast = tmdb_client.get_single_movie_cast(1)
    assert cast == mock_cast
