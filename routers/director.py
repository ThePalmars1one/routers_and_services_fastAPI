from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.director import Director
from config.database import Session
from service.director import DirectorService


director_router = APIRouter()

@director_router.get('/director/',tags=['director'], response_model=Director, status_code= 200)
def get_directors() -> Director:   
    db = Session()
    result = DirectorService(db).get_director()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@director_router.post('/director/',tags=['director'], status_code= 201 , response_model=dict)
def create_director(director:Director) -> dict:
    db= Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={'message':'Director saved in data base'}, status_code=201)

@director_router.delete('/director/{id}',tags=['director'])
def delete_directors(id:int):
    db = Session()
    success = DirectorService(db).delete_director(id)
    if success:
        return JSONResponse(content="Deleted director", status_code=200)
    else:
        return JSONResponse(status_code=404,content={"message":"Not found"})

@director_router.put('/director{id}',tags=['director'])
def update_genre(id:int,director:Director):
    db =  Session()
    result = DirectorService(db).get_director_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    DirectorService(db).update_director(id, director)
    return JSONResponse(content={"message":"Se ha modificado el director con id: " + str(id)})

