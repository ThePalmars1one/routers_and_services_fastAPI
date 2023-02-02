from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.reviewer import Reviewer
from config.database import Session
from service.reviewer import ReviewerService


reviewer_router = APIRouter()

@reviewer_router.get('/reviewer/',tags=['reviewer'], response_model=Reviewer, status_code= 200)
def get_reviewers() -> Reviewer:   
    db = Session()
    result = ReviewerService(db).get_reviewer()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@reviewer_router.post('/reviewer',tags=['reviewer'], status_code= 201 , response_model=dict)
def create_reviewer(reviewer:Reviewer) -> dict:
    db= Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={'message':'Reviewer saved in data base'}, status_code=201)


