
from app.extensions.extensions import db
class Movie(db.Model):
    __tablename__="movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
