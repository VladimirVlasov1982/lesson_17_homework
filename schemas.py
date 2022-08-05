# Схемы моделей
from marshmallow import Schema, fields

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

class DirectorSchema(Schema):
    """Схема режиссера"""
    id = fields.Int()
    name = fields.Str()

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