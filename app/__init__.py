from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///lateshow.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import episodes_bp, guests_bp, appearances_bp
    app.register_blueprint(episodes_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(appearances_bp)

    @app.route('/')
    def index():
        return 'Welcome to the Late Show API!'

    return app

