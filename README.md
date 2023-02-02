# Routers and Services Practice (FastAPI)
In this repository you can find routes and services using the fastAPI framework, and the implementation of HTTP verbs: GET, POST, PUT and DELETE.

First you need to clone the repository with the command:

git clone https://github.com/ThePalmars1one/routers_and_services_fastAPI.git

After you have cloned the repository, you must verify that you have PIP installed, if you are using Python 2.7.9 (or higher) or Python 3.4 (or higher), then PIP comes installed with Python by default. To check the version, the command is:

pip --version

## VENV
After following these steps you must create a virtual environment and activate it:

1. python -m venv venv_name

2. source venv_name/Scripts/activate (GIT BASH)

To deactivate the environment just type in the console: deactivate.

## Requirements.txt
The next step would be to install all the packages required in the project, which are described in the requirements.txt, with the following command and run it:

1. pip install -r requirements.txt

2. uvicorn main:app --reload

## Routers
This would be an example of the implementation of "GET" in the "movie" routes:

@genres_router.get('/genres',tags=['genres'], response_model=Genres, status_code= 200)
def get_genre() -> Genres:   
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

With this code a request is made and, if successful, the code: 200 OK is displayed, confirming that all relevant information has been retrieved.

## Services
This is the service used in the previous example:

def get_genres(self) -> genresModel:
        result = self.db.query(genresModel).all()
        return result

With this function the connection with the database is made, the query to the "genresModel" is made and with the function ".all()" bring all that it finds.