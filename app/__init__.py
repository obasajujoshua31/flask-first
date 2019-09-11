from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config



def create_app(config_name, db):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    from app.models import BucketList
    return app