from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

from .. import login_manager
from .base import Base


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column("phone_number", String(11), nullable=False, unique=True)
    _password = Column("password", String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self.password, raw)


@login_manager.user_loader
def load_user(uid):
    return User.query.filter_by(id=uid).first()
