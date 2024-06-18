from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Initialize SQLAlchemy and Migrate objects
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from app.config.Config

    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints and register them with the app
    from .routes import episodes_bp, guests_bp, appearances_bp
    app.register_blueprint(episodes_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(appearances_bp)

    return app
