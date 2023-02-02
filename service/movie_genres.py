from models.movie_genres import MovieGenres as movieGenresModel

class MovieGenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_movie_genres(self) -> movieGenresModel:
        result = self.db.query(movieGenresModel).all()
        return result

    def create_movie_genre(self,movie_genre:movieGenresModel):
        new_movie_genre = movieGenresModel(
        mov_id = movie_genre.mov_id,
        gen_id = movie_genre.gen_id
        )
        self.db.add(new_movie_genre)
        self.db.commit()
        return

    