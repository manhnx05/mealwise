from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Load config
    from config import Config
    app.config.from_object(Config)

    # Init extensions
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    with app.app_context():
        from . import models  # noqa: F401 - import để SQLAlchemy nhận diện models
        db.create_all()       # Tự tạo bảng nếu chưa tồn tại

        from . import routes
        app.register_blueprint(routes.bp)

    return app
