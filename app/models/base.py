from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import BaseQuery, SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

from ..lib.helper import set_query_conditions


class CustomQuery(BaseQuery):
    @set_query_conditions(status=1)
    def filter_by(self, **kwargs):
        return super().filter_by(**kwargs)


db = SQLAlchemy(query_class=CustomQuery)


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    create_time = Column("create_time", Integer, nullable=False)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @classmethod
    @contextmanager
    def auto_commit(cls):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def add_attrs(self, **attrs):
        for k, v in attrs.items():
            if hasattr(self, k) and k != "id":
                setattr(self, k, v)
