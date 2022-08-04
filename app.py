from flask import request
from flask_paginate import get_page_parameter
from config import app, api, PER_PAGE
from flask_restx import Resource
from models import *

movie_ns = api.namespace('movies')
genre_ns = api.namespace('genres')
director_ns = api.namespace('directors')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Возвращает список всех фильмов.
        Возвращает фильмы по id режиссера и по id жанра.
        Возвращает только фильмы с определенным режиссером и жанром по их id
        """
        req_director = request.args.get('director_id')
        req_genre = request.args.get('genre_id')
        if req_director and req_genre:
            movies = Movie.query.filter(Movie.director_id == req_director, Movie.genre_id == req_genre).all()
            return movies_shema.dump(movies), 200
        if req_director:
            movies = Movie.query.filter(Movie.director_id == req_director).all()
            return movies_shema.dump(movies), 200
        if req_genre:
            movies = db.session.query(Movie).filter(Movie.genre_id == req_genre).all()
            return movies_shema.dump(movies)
        page = request.args.get(get_page_parameter(), type=int, default=1)
        movies = db.session.query(Movie).limit(PER_PAGE).offset((page - 1) * PER_PAGE).all()
        return movies_shema.dump(movies), 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        """
        Возвращает фильм по id
        """
        try:
            movie = db.session.query(Movie).get(mid)
            return movie_shema.dump(movie), 200
        except:
            return "", 404


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        """
        Возвращает список режиссеров
        """
        directors = Director.query.all()
        return directors_shema.dump(directors), 200

    def post(self):
        """
        Добавляет режиссера
        """
        req_json = request.json
        director = Director(**req_json)
        db.session.add(director)
        db.session.commit()
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def put(self, did: int):
        """
        Обновление режиссера
        """
        try:
            director = Director.query.get(did)
            req_json = request.json
            if "name" in req_json:
                director.name = req_json.get("name")
                db.session.add(director)
                db.session.commit()
                return "", 204
        except:
            return "", 404

    def delete(self, did: int):
        """
        Удаление режиссера
        """
        try:
            director = Director.query.get(did)
            db.session.delete(director)
            db.session.commit()
            return "", 204
        except:
            return "", 404


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Возвращает список жанров
        """
        genres = db.session.query(Genre).all()
        return genres_shema.dump(genres), 200

    def post(self):
        """
        Добавляет жанр
        """
        req_json = request.json
        genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(genre)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def put(self, gid: int):
        """
        Обновление жанра
        """
        try:
            genre = Genre.query.get(gid)
            req_json = request.json
            if "name" in req_json:
                genre.name = req_json.get("name")
                db.session.add(genre)
                db.session.commit()
                return "", 204
        except:
            return "", 404

    def delete(self, gid: int):
        """
        Удаление жанра
        """
        try:
            genre = Genre.query.get(gid)
            db.session.delete(genre)
            db.session.commit()
            return "", 204
        except:
            return "", 404


if __name__ == '__main__':
    app.run(debug=True)
