import os
import uuid
from flask import Flask
from flask_smorest import Api
from resources.store import blp as StoreBluePrint
from resources.item import blp as ItemBluePrint
from resources.tag import blp as TagBluePrint
from db import db
from urllib.parse import quote_plus


def create_app(db_url = None):
    # Replace special characters in the password with their percent-encoded values
    password = "Password@123"  # Your actual password here
    _password = quote_plus(password)

    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Store REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "postgresql://postgres:{0}@localhost/flask_demo".format(_password)
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)

    api = Api(app)
    api.register_blueprint(StoreBluePrint)
    api.register_blueprint(ItemBluePrint)
    api.register_blueprint(TagBluePrint)

    app.run(debug=True)
    return app

if __name__ == "__main__":
    create_app()
