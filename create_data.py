# create_data.py

# чтобы создать БД с данными
import json

from models import *
from run import db


def insert_data(model, input_data):
    for row in input_data:
        db.session.add(model(**row))
        db.session.commit()


def init_base():
    db.drop_all()
    db.create_all()

    with open('fixtures/movies.json', "r", encoding="utf-8") as file:
        insert_data(Movie, json.load(file))

    with open('fixtures/direcors.json', "r", encoding="utf-8") as file:
        insert_data(Director, json.load(file))

    with open('fixtures/genres.json', "r", encoding="utf-8") as file:
        insert_data(Genre, json.load(file))


init_base()
