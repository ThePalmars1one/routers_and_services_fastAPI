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

@genres_router.delete('/genres/{id}',tags=['genres'])
def delete_genre(id:int):
    db = Session()
    success = GenresService(db).delete_genre(id)
    if success:
        return JSONResponse(content="Deleted genre", status_code=200)
    else:
        return JSONResponse(status_code=404,content={"message":"Not found"})

@genres_router.put('/genres{id}',tags=['genres'])
def update_genre(id:int,genre:Genres):
    db =  Session()
    result = GenresService(db).get_genre_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    GenresService(db).update_genre(id, genre)
    return JSONResponse(content={"message":"Se ha modificado el genero con id: " + str(id)})

