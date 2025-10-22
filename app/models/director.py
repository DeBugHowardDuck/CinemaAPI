
from app.extensions.extensions import db
class Director(db.Model):
    __tablename__="directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
