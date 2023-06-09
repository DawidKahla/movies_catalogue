from flask import Flask, render_template, request, redirect, url_for
import tmdb_client

app = Flask(__name__)


@app.route("/")
def homepage():
    selected_list = request.args.get("list_name", "popular")
    if selected_list not in tmdb_client.list_of_types:
        return redirect(url_for("homepage", list_name="popular"))
    movies = tmdb_client.get_movies(how_many=8, list_name=selected_list)
    return render_template(
        "homepage.html",
        movies=movies,
        list_name=selected_list,
        list_of_types=tmdb_client.list_of_types,
    )


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id=movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id=movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


if __name__ == "__main__":
    app.run(debug=True)
