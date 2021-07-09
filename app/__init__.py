from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/setting.py")
    register_blueprint(app)
    return app


def register_blueprint(app):
    from .manager.blueprint import web
    app.register_blueprint(web)
