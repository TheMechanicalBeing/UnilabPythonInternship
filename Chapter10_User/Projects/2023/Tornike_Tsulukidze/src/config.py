from os import path


class Config(object):
    SECRET_KEY = "SECRET"
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))

    TEPMLATE_FOLDER = path.join(BASE_DIRECTORY, "templates")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIRECTORY}/database.sqlite"
