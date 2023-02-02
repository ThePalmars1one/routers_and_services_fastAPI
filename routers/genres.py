from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.genres import Genres
from config.database import Session
from service.genres import GenresService


genres_router = APIRouter()

@genres_router.get('/genres',tags=['genres'], response_model=Genres, status_code= 200)
def get_genre() -> Genres:   
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.post('/genres',tags=['genres'], status_code= 201 , response_model=dict)
def create_genre(genre:Genres) -> dict:
    db= Session()
    GenresService(db).create_genre(genre)
    return JSONResponse(content={'message':'genre save in data base'}, status_code=201)

