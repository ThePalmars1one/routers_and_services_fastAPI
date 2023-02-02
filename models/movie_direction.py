from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.reviewer import Reviewer


class MovieDirection(Base):

    __tablename__ = "movie_direction"

    id = Column(Integer, primary_key=True, index=True)
    dir_id = Column(Integer, ForeignKey("director.dir_id"))
    mov_id = Column(Integer, ForeignKey("movie.id"))
    