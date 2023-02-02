from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.genres import Genres


class MovieGenres(Base):

    __tablename__ = "movie_genres"

    mov_id = Column(Integer, ForeignKey("movie.id"))
    gen_id = Column(Integer, ForeignKey("genres.gen_id"))