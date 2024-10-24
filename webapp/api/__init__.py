from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from database import db
from .controllers.default import default_bp

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        app.register_blueprint(default_bp)

    return app
