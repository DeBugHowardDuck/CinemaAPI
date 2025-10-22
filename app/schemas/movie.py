
from app.extensions.extensions import ma
from marshmallow import fields
class MovieSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre_id = fields.Int()
    director_id = fields.Int()
class MovieRequestSchema(ma.Schema):
    title = fields.Str(required=True)
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre_id = fields.Int()
    director_id = fields.Int()
