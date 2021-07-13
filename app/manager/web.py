from flask import render_template
from flask_login import login_required

from .blueprint import web


@web.route("/")
def index():
    return render_template("index.html")


@web.route("/customer")
@login_required
def customer():
    return render_template("customer.html")
