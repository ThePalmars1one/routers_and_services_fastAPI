from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from config.database import Base
from models.reviewer import Reviewer


class rating(Base):

    __tablename__ = "rating"

    mov_id = Column(Integer, ForeignKey("movie.id"))
    rev_id = Column(Integer, ForeignKey("reviewer.rev_id"))
    rev_stars = Column(Float)
    num_o_ratings = Column(Integer)