
from app.extensions.extensions import ma
from marshmallow import fields
class UserSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True)
    surname = fields.Str()
    favorite_genre = fields.Int()
class UserRequestSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    surname = fields.Str()
    favorite_genre = fields.Int()
