
import os
from flask import Flask
from dotenv import load_dotenv
from config import DevelopmentConfig
from app.extensions.extensions import db, api, ma
from app.utils.logger import setup_logger
from app.utils.error_handlers import register_error_handlers

def create_app(config_object=DevelopmentConfig):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    uri = app.config.get("SQLALCHEMY_DATABASE_URI","")
    if uri.startswith("sqlite:///") and uri != "sqlite:///:memory:":
        db_path = uri.replace("sqlite:///", "")
        if not os.path.isabs(db_path):
            project_root = os.path.abspath(os.path.join(app.root_path, ".."))
            db_path = os.path.abspath(os.path.join(project_root, db_path))
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path.replace(os.sep, "/")

    from app.views.health import health_ns
    from app.views.auth import auth_ns
    from app.views.movies import movie_ns
    from app.views.genres import genre_ns
    from app.views.directors import director_ns
    from app.views.user import user_ns
    from app.views.favorites import favorites_ns

    api.add_namespace(health_ns, path="/health")
    api.add_namespace(auth_ns, path="/auth")
    api.add_namespace(movie_ns, path="/movies")
    api.add_namespace(genre_ns, path="/genres")
    api.add_namespace(director_ns, path="/directors")
    api.add_namespace(user_ns, path="/users")
    api.add_namespace(favorites_ns, path="/favorites")

    register_error_handlers(app)
    setup_logger()
    with app.app_context():
        db.create_all()
    return app
