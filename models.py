# Модели и их схемы
from config import db
from marshmallow import Schema, fields


class Movie(db.Model):
    """Модель фильма"""
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """Схема фильма"""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Nested('GenreSchema', many=False, only=['name'])
    director = fields.Nested('DirectorSchema', many=False, only=['name'])


class Director(db.Model):
    """Модель режиссера"""
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """Схема режиссера"""
    id = fields.Int()
    name = fields.Str()


class Genre(db.Model):
    """Модель жанра"""
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """Схема жанра"""
    id = fields.Int()
    name = fields.Str()


movie_shema = MovieSchema()
movies_shema = MovieSchema(many=True)

director_shema = DirectorSchema()
directors_shema = DirectorSchema(many=True)

genre_shema = GenreSchema()
genres_shema = GenreSchema(many=True)
