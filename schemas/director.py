from typing import Optional
from pydantic import BaseModel, Field


class Actor(BaseModel):
        dir_id: Optional[int] = None
        dir_fname: str = Field(max_length=15,min_length=3)
        dir_lname: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    "actor_first_name": "Ridley",
                    "actor_last_name":"Scott",
                }
            }