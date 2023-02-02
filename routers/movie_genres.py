from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.movie_genres import MovieGenres
from config.database import Session
from service.movie_genres import MovieGenresService


movie_genres_router = APIRouter()

@movie_genres_router.get('/moviegenres/',tags=['movie_genres'], response_model=MovieGenres, status_code= 200)
def get_movie_genre() -> MovieGenres:   
    db = Session()
    result = MovieGenresService(db).get_movie_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_genres_router.post('/moviegenres/',tags=['movie_genres'], status_code= 201 , response_model=dict)
def create_movie_genre(movie_genre:MovieGenres) -> dict:
    db= Session()
    MovieGenresService(db).create_movie_genre(movie_genre)
    return JSONResponse(content={'message':'Movie Genre saved in data base'}, status_code=201)

