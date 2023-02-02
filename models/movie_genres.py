from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from config.database import Base

class MovieGenres(Base):

    __tablename__ = "movie_genres"

    id = Column(Integer, primary_key=True, index=True)
    gen_id = Column(Integer, ForeignKey("genres.gen_id"))
    mov_id = Column(Integer, ForeignKey("movie.id"))
    