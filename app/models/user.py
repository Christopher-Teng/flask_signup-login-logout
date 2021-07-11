from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

from .base import Base, db


class User(Base):
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
