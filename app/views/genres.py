from flask_restx import Namespace, Resource, fields
from flask import request
from app.extensions.extensions import db, api
from app.models.genre import Genre

genre_ns = Namespace("genres", description="Жанры")
genre_model = api.model("Genre", {"id": fields.Integer, "name": fields.String(required=True)})


@genre_ns.route("")
class Genres(Resource):
    @genre_ns.marshal_list_with(genre_model)
    def get(self): return db.session.query(Genre).all()

    @genre_ns.expect(genre_model)
    @genre_ns.marshal_with(genre_model, code=201)
    def post(self):
        from app.utils.auth import auth_required
        @auth_required
        def _inner():
            g = Genre(name=(request.json or {}).get("name", ""))
            db.session.add(g);
            db.session.commit();
            return g, 201

        return _inner()
