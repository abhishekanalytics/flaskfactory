 # myapp/__init__.py
from flask import Flask
from .config import Config
from .views import main_blueprint


# app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_blueprint)


    return app

