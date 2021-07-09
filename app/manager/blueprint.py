from flask import Blueprint

web = Blueprint("web", __name__, url_prefix="/")

auth = Blueprint("auth", __name__, url_prefix="/user")
