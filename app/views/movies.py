
from flask_restx import Namespace, Resource, fields
from flask import request
from app.extensions.extensions import db, api
from app.models.movie import Movie
from sqlalchemy import asc, desc

movie_ns = Namespace("movies", description="Фильмы")
movie_model = api.model("Movie", {
    "id": fields.Integer,
    "title": fields.String(required=True),
    "description": fields.String,
    "trailer": fields.String,
    "year": fields.Integer(required=True),
    "rating": fields.Float(required=True),
    "genre_id": fields.Integer,
    "director_id": fields.Integer
})

@movie_ns.route("")
class Movies(Resource):
    def get(self):
        page = max(int((request.args.get("page") or 1)), 1)
        per_page = min(max(int((request.args.get("per_page") or 20)), 1), 100)
        q = db.session.query(Movie)

        if request.args.get("genre_id"):    q = q.filter(Movie.genre_id == int(request.args["genre_id"]))
        if request.args.get("director_id"): q = q.filter(Movie.director_id == int(request.args["director_id"]))
        if request.args.get("year"):        q = q.filter(Movie.year == int(request.args["year"]))
        if request.args.get("search"):
            kw = f"%{request.args['search']}%"
            q = q.filter(Movie.title.ilike(kw))

        sort = (request.args.get("sort") or "id")
        order = (request.args.get("order") or "desc")
        col = getattr(Movie, sort, Movie.id)
        q = q.order_by(desc(col) if order == "desc" else asc(col))

        total = q.count()
        items = q.offset((page-1)*per_page).limit(per_page).all()
        def dump(m):
            return dict(id=m.id, title=m.title, description=m.description, trailer=m.trailer,
                        year=m.year, rating=m.rating, genre_id=m.genre_id, director_id=m.director_id)
        return {"items": [dump(m) for m in items], "total": total, "page": page, "per_page": per_page}, 200

    @movie_ns.expect(movie_model)
    @movie_ns.marshal_with(movie_model, code=201)
    def post(self):
        from app.utils.auth import auth_required
        @auth_required
        def _create():
            data = request.json or {}
            m = Movie(**{k: v for k, v in data.items() if k in Movie.__table__.columns.keys()})
            db.session.add(m); db.session.commit(); return m, 201
        return _create()

@movie_ns.route("/<int:movie_id>")
class MovieById(Resource):
    @movie_ns.marshal_with(movie_model)
    def get(self, movie_id):
        obj = db.session.get(Movie, movie_id)
        return (obj, 200) if obj else ({}, 404)

    def put(self, movie_id):
        from app.utils.auth import auth_required
        @auth_required
        def _update():
            obj = db.session.get(Movie, movie_id)
            if not obj: return {"message":"Not found"}, 404
            data = request.json or {}
            for k, v in data.items():
                if k in Movie.__table__.columns.keys() and k != "id":
                    setattr(obj, k, v)
            db.session.commit()
            return {"message":"updated","id":obj.id}, 200
        return _update()

    def delete(self, movie_id):
        from app.utils.auth import auth_required
        @auth_required
        def _delete():
            obj = db.session.get(Movie, movie_id)
            if not obj: return {"message":"Not found"}, 404
            db.session.delete(obj); db.session.commit(); return "", 204
        return _delete()
