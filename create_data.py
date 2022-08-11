# чтобы создать БД с данными
import json

from config import DevConfig
from models import Movie, Director, Genre
from app import create_app, db

app = create_app(DevConfig)
app.app_context().push()


def insert_data(model, input_data):
    """
    Загрузка данных в таблицы
    """
    for row in input_data:
        db.session.add(model(**row))
        db.session.commit()


def init_base():
    """
    Создание таблиц
    """
    db.drop_all()
    db.create_all()

    with open('fixtures/movies.json', "r", encoding="utf-8") as file:
        insert_data(Movie, json.load(file))

    with open('fixtures/direcors.json', "r", encoding="utf-8") as file:
        insert_data(Director, json.load(file))

    with open('fixtures/genres.json', "r", encoding="utf-8") as file:
        insert_data(Genre, json.load(file))


init_base()
