from datetime import timedelta

DEBUG = True
SECRET_KEY = "!@#$%^&*"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/flask"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATION = True
REMEMBER_COOKIE_DURATION = timedelta(days=7)
REMEMBER_COOKIE_HTTPONLY = True
