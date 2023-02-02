from models.movie_direction import MovieDirection as movieDirectionModel

class MovieDirectionService():
    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self) -> movieDirectionModel:
        result = self.db.query(movieDirectionModel).all()
        return result

    def create_movie_direction(self,movie_direction:movieDirectionModel):
        new_movie_direction = movieDirectionModel(
        dir_id = movie_direction.dir_id,
        mov_id = movie_direction.mov_id
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return

    