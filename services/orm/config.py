from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utility.commons import USER, DB_PASS, HOST, DB
db = SQLAlchemy()
migrate = Migrate()


class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{DB_PASS}@{HOST}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
