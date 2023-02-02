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

