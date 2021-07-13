from flask import flash, redirect, render_template, request, url_for
from flask_login import login_manager, login_user, logout_user
from flask_login.utils import login_required

from ..forms.auth import LoginForm, UserForm
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
    form = LoginForm()
    if form.validate_on_submit():
        email_or_phone_number = request.form.get("email_or_phone_number")
        password = request.form.get("password")
        remember_me = True if request.form.get("remember_me") else False
        user = _login(email_or_phone_number)
        if user and user.check_password(password):
            login_user(user, remember=remember_me)
            next = request.args.get("next")
            print("next: {}".format(next))
            next = next if next and next.startswith("/") else "/"
            return redirect(next)
        flash(u"用户不存在或密码错误！")
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("web.index"))


def _login(email_or_phone_number):
    user = User.query.filter_by(
        email=email_or_phone_number).first() or User.query.filter_by(
        phone_number=email_or_phone_number).first()
    return user
