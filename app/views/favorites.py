from flask_restx import Namespace, Resource, fields
from app.extensions.extensions import db, api
from app.models.favorite import favorites

favorites_ns = Namespace("favorites", description="Избранное")
fav_model = api.model("Favorite", {"user_id": fields.Integer, "movie_id": fields.Integer})


@favorites_ns.route("/<int:user_id>/<int:movie_id>")
class Fav(Resource):
    def post(self, user_id, movie_id):
        from app.utils.auth import auth_required
        @auth_required
        def _inner():
            db.session.execute(favorites.insert().values(user_id=user_id, movie_id=movie_id))
            db.session.commit();
            return "", 204

        return _inner()

    def delete(self, user_id, movie_id):
        from app.utils.auth import auth_required
        @auth_required
        def _inner():
            db.session.execute(
                favorites.delete().where((favorites.c.user_id == user_id) & (favorites.c.movie_id == movie_id)))
            db.session.commit();
            return "", 204

        return _inner()
