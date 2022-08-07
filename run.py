from config import DevConfig, PER_PAGE
from flask import request
from flask_restx import Resource, Api
from models import Movie, Director, Genre
from schemas import *
from flask_paginate import get_page_parameter
from app import create_app, db

app = create_app(DevConfig)
api = Api(app)

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

    def post(self):
        """
        Добавление фильма
        """
        req_json = request.json
        movie = Movie(**req_json)
        db.session.add(movie)
        db.session.commit()
        return movie_shema.dump(movie), 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        """
        Возвращает фильм по id
        """
        movie = db.session.query(Movie).get(mid)
        if movie:
            return movie_shema.dump(movie), 200
        return "", 404

    def put(self, mid: int):
        """
        Обновление фильма
        """
        try:
            req_json = request.json
            movie = Movie.query.get(mid)
            if "title" in req_json:
                movie.title = req_json.get("title")
                db.session.add(movie)
                db.session.commit()
            if "description" in req_json:
                movie.description = req_json.get("description")
                db.session.add(movie)
                db.session.commit()
            if "trailer" in req_json:
                movie.trailer = req_json.get("trailer")
                db.session.add(movie)
                db.session.commit()
            if "year" in req_json:
                movie.year = req_json.get("year")
                db.session.add(movie)
                db.session.commit()
            if "rating" in req_json:
                movie.rating = req_json.get("rating")
                db.session.add(movie)
                db.session.commit()
            if "genre_id" in req_json:
                movie.genre_id = req_json.get("genre_id")
                db.session.add(movie)
                db.session.commit()
            if "director_id" in req_json:
                movie.director_id = req_json.get("director_id")
                db.session.add(movie)
                db.session.commit()
            return movie_shema.dump(movie), 204
        except:
            return "", 404

    def delete(self, mid: int):
        """
        Удаление фильма по его id
        """
        try:
            movie = Movie.query.get(mid)
            db.session.delete(movie)
            db.session.commit()
            return "Фильм удален", 204
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
        return director_shema.dump(director), 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        """
        Возвращает режиссера по его id
        """
        director = Director.query.get(did)
        if director:
            return director_shema.dump(director), 200
        return "", 404

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
            return director_shema.dump(director), 204
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
        try:
            req_json = request.json
            genre = Genre(**req_json)
            with db.session.begin():
                db.session.add(genre)
            return genre_shema.dump(genre), 201
        except:
            return "", 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid: int):
        """
        Возвращает жанр по его id
        """
        genre = Genre.query.get(gid)
        if genre:
            return genre_shema.dump(genre), 200
        return "", 404

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
            return genre_shema.dump(genre), 204
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
    app.run()
