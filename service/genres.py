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

    def delete_genre(self, id:int):
        genre = self.db.query(genresModel).get(id)
        if genre:
            self.db.delete(genre)
            self.db.commit()
            return True
        return False

    def update_genre(self,id:int, data:genresModel):
        genre = self.db.query(genresModel).get(id)
        if genre:
            genre.gen_title = data.gen_title
            self.db.commit()
            return True
        return False

    def get_genre_id(self,id:int):
        result = self.db.query(genresModel).filter(genresModel.gen_id == id).first()
        return result

    