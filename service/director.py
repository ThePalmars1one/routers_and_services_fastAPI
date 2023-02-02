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

    def delete_director(self, id:int):
        director = self.db.query(directorModel).get(id)
        if director:
            self.db.delete(director)
            self.db.commit()
            return True
        return False

    def update_director(self,id:int, data:directorModel):
        director = self.db.query(directorModel).get(id)
        if director:
            director.dir_fname = data.dir_fname
            director.dir_lname = data. dir_lname
            self.db.commit()
            return True
        return False

    def get_director_id(self,id:int):
        result = self.db.query(directorModel).filter(directorModel.dir_id == id).first()
        return result

    