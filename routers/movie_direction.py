from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.movie_direction import MovieDirection
from config.database import Session
from service.movie_direction import MovieDirectionService


movie_direction_router = APIRouter()

@movie_direction_router.get('/moviedirection',tags=['movie_direction'], response_model=MovieDirection, status_code= 200)
def get_movie_direction() -> MovieDirection:   
    db = Session()
    result = MovieDirectionService(db).get_movie_direction()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_direction_router.post('/moviedirection',tags=['movie_direction'], status_code= 201 , response_model=dict)
def create_movie_direction(movie_direction:MovieDirection) -> dict:
    db= Session()
    MovieDirectionService(db).create_movie_direction(movie_direction)
    return JSONResponse(content={'message':'Movie Direction saved in data base'}, status_code=201)

