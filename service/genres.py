from models.genres import Genres as genresModel

class GenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self) -> genresModel:
        result = self.db.query(genresModel).all()
        return result

    def create_genre(self,genre:genresModel):
        new_genre = genresModel(
        gen_id = genre.gen_id,
        gen_title = genre.gen_title
        )
        self.db.add(new_genre)
        self.db.commit()
        return

    