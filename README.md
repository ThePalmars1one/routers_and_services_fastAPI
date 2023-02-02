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

<p align=center>
<img src="https://i.postimg.cc/qRMmn5sD/get-genres-router.png">
</p>

Session() is what will allow us to perform CRUD queries, which is stored in the variable "db", then it is passed as a parameter to the service and the function that will perform the request is called. "jsonable_encoder" is simply in charge of encoding the information to JSON format and at the end of the process, a code "200" is returned to indicate that the query was successful.

## Services
This is the service used in the previous example:

<p align=center>
<img src="https://i.postimg.cc/1RDHXP1R/get-genres-service.png">
</p>

With this function the connection with the database is made, the query to the "genresModel" is made and with the function ".all()" bring all that it finds.


