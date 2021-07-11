from flask import flash, redirect, render_template, url_for

from ..forms.auth import UserForm
from ..models.base import db
from ..models.user import User
from .blueprint import auth


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    if form.validate_on_submit():
        nickname = form.data.get("nickname")
        email = form.data.get("email")
        phone_number = form.data.get("phone_number")
        password = form.data.get("password")
        if _check_registed(email=email):
            flash(u"邮箱已被注册！")
            return render_template("register.html", form=form)
        if _check_registed(phone_number=phone_number):
            flash(u"手机号码已被注册！")
            return render_template("register.html", form=form)
        user = User()
        user.add_attrs(nickname=nickname, email=email, phone_number=phone_number, password=password)
        try:
            with User.auto_commit():
                db.session.add(user)
            return redirect(url_for("auth.login"))
        except Exception as _:
            flash(u"注册失败！")
    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return "<h1>Login page</h1>"


def _check_registed(email=None, phone_number=None):
    if email:
        if User.query.filter_by(email=email).first():
            return True
    if phone_number:
        if User.query.filter_by(phone_number=phone_number).first():
            return True
    return False
