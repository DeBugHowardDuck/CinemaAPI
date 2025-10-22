
from flask_restx import Namespace, Resource, fields
from app.extensions.extensions import db, api
from app.models.user import User
user_ns = Namespace("users", description="Пользователи")
user_model = api.model("User", {"id":fields.Integer,"email":fields.String,"name":fields.String})
@user_ns.route("")
class Users(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self): return db.session.query(User).all()
