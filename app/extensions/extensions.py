
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
api = Api(title="КиноБаза API", version="1.2", description="Документация к API КиноБазы", doc="/", hide_models=False)
ma = Marshmallow()
