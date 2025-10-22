from flask_restx import Namespace, Resource, fields
from flask import request
from app.extensions.extensions import db, api
from app.models.director import Director

director_ns = Namespace("directors", description="Режиссёры")
director_model = api.model("Director", {"id": fields.Integer, "name": fields.String(required=True)})


@director_ns.route("")
class Directors(Resource):
    @director_ns.marshal_list_with(director_model)
    def get(self): return db.session.query(Director).all()

    @director_ns.expect(director_model)
    @director_ns.marshal_with(director_model, code=201)
    def post(self):
        from app.utils.auth import auth_required
        @auth_required
        def _inner():
            d = Director(name=(request.json or {}).get("name", ""))
            db.session.add(d);
            db.session.commit();
            return d, 201

        return _inner()
