
import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI","sqlite:///C:/kinobaza_data/instance/kinobaza.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET = os.getenv("JWT_SECRET","dev-secret")
    RESTX_MASK_SWAGGER = False
class DevelopmentConfig(Config): ...
