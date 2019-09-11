from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config
db = SQLAlchemy()




def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    from app.models import BucketList



    @app.route("/")
    def home():
        return jsonify({
            "name": "This is home"
        })


    @app.route('/bucketlists/', methods=["POST", "GET"])
    def bucketlist():
        if request.method == "GET":
            bucketlists = BucketList.get_all()
            results = []
            for bucketlist in bucketlists:
                results.append({
                    "id": bucketlist.id,
                    "name": bucketlist.name,
                    "created_on": bucketlist.date_created,
                    "date_modified": bucketlist.date_modified
                })
            response = jsonify(results)
            response.status_code = 200
            return response
        elif request.method == "POST":
            name = str(request.form.get("name", ""))
            bucketlist = BucketList(name=name)
            bucketlist.save()
            response = jsonify({
                "id": bucketlist.id,
                "name": bucketlist.name,
                "created_at": bucketlist.date_created,
                "date_modified": bucketlist.date_modified
            })
            response.status_code = 201
            return response
        else:
            return jsonify({
                "key": "others"
            })
    return app