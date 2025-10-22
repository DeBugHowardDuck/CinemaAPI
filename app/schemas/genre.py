
from app.extensions.extensions import ma
from marshmallow import fields
class GenreSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
