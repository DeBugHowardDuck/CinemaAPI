
from flask_restx import Namespace, Resource, fields
from flask import request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions.extensions import db, api
from app.models.user import User
from app.utils.jwt_helper import generate_jwt

auth_ns = Namespace("auth", description="Аутентификация")

register_model = api.model("RegisterRequest", {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "name": fields.String(required=True),
})

@auth_ns.route("/register")
class Register(Resource):
    @auth_ns.expect(register_model)
    def post(self):
        data = request.json or {}
        if not data.get("email") or not data.get("password"):
            return {"message":"email and password required"},400
        if db.session.query(User).filter_by(email=data["email"]).first():
            return {"message":"user exists"},409
        u = User(email=data["email"], password=generate_password_hash(data["password"]), name=data.get("name",""))
        db.session.add(u); db.session.commit()
        return {"id": u.id, "email": u.email}, 201

login_model = api.model("LoginRequest", {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
})

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = request.json or {}
        u = db.session.query(User).filter_by(email=data.get("email")).first()
        if not u or not check_password_hash(u.password, data.get("password","")):
            return {"message":"invalid credentials"},401
        token = generate_jwt(u.id, current_app.config["JWT_SECRET"])
        return {"token": token}
