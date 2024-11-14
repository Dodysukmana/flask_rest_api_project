# app/__init__.py
from flask import Flask
from .config import Config
from .models import db
from .routes import init_routes
from flask_migrate import Migrate  # Import Flask-Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)  # Tambahkan inisialisasi Flask-Migrate

    # Register routes
    init_routes(app)

    return app
