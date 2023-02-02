from typing import Optional
from pydantic import BaseModel, Field



class MovieCast(BaseModel):
        gen_id: int
        mov_id: int

        class Config:
            schema_extra = {
                "example":{
                    "gen_id": 1,
                    "mov_id": 1
                }
            }