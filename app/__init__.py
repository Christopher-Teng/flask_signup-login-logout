from flask import Flask
from flask_wtf import CsrfProtect


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/setting.py")
    csrf = CsrfProtect()
    csrf.init_app(app)
    register_blueprint(app)
    create_db(app)
    return app


def register_blueprint(app):
    from .manager.blueprint import auth, web
    app.register_blueprint(web)
    app.register_blueprint(auth)


def create_db(app):
    from .models.base import db
    db.init_app(app)
    db.create_all(app=app)
