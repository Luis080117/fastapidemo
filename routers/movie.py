from fastapi import APIRouter, Depends
from models.movies import Movie
from services.movie_service import *
from config.mongo_connection import *
from models.movies import *
from schemas.movies import Movie, MovieCreate
from schemas.bearer import JWTBearer

connection = connect_to_mongodb('test', 'movies')
router_movies = APIRouter()

@router_movies.get('/movies', tags=["Movies"], dependencies=[Depends(JWTBearer())])
def get_movies_function():
    return get_movies()

@router_movies.get('/movie/', tags=["Movies"], dependencies=[Depends(JWTBearer())])
def get_movie_function(movie_title: str):
    return get_movie(movie_title)

@router_movies.post('/movie/', tags=["Movies"], dependencies=[Depends(JWTBearer())])
def create_movie_function(movie: MovieCreate):
    return create_movie(movie)

@router_movies.put('/movie/', tags=["Movies"], dependencies=[Depends(JWTBearer())])
def update_movie_function(movie_title: str, movie: MovieCreate):
    return update_movie(movie_title, movie)

@router_movies.delete('/movie/', tags=["Movies"], dependencies=[Depends(JWTBearer())])
def delete_movie_function(movie_title: str):
    return delete_movie(movie_title)