from models.director import Director as directorModel

class DirectorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_director(self) -> directorModel:
        result = self.db.query(directorModel).all()
        return result

    def create_director(self,director:directorModel):
        new_director = directorModel(
        dir_id = director.dir_id,
        dir_fname = director.dir_fname,
        dir_lname = director.dir_lname
        )
        self.db.add(new_director)
        self.db.commit()
        return

    