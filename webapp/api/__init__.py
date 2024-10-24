from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from database import db
from .controllers.default import default_bp

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:5000","https://desafio-tech-bice.vercel.app", "https://desafio-tech-back.vercel.app"]}})

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        app.register_blueprint(default_bp)

    return app
