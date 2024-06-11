import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://yourusername:yourpassword@localhost/lateshow_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
