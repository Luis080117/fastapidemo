from models.movies import Movie
from schemas.movies import MovieCreate

def create_movie(movie: MovieCreate):
    movie = Movie(title=movie.title, year=movie.year)
    movie.save()
    return {"message": "Movie created successfully"}

def get_movies():
    movies = Movie.objects()
    serialized_movies = [{"_id": str(movie.id), "title": movie.title, "year": movie.year} for movie in movies]
    return {"movies": serialized_movies}

def get_movie(movie_title: str) -> dict:
    movie = Movie.objects(title=movie_title)
    serialized_movie = [{"_id": str(movie.id), "title": movie.title, "year": movie.year} for movie in movie]
    return {"movie": serialized_movie}

def delete_movie(movie_title: str):
    movie = Movie.objects(title=movie_title)
    if movie:
        movie.delete()
        return {"message": "Movie deleted successfully"}
    else:
        return {"error": "Movie not found"}

def update_movie(movie_title: str, new_movie: MovieCreate):
    existing_movie = Movie.objects(title=movie_title).first()
    if not existing_movie:
        return "No movie found"
    existing_movie.title = new_movie.title
    existing_movie.year = new_movie.year
    existing_movie.save()
    return {"message": "Movie updated successfully"}