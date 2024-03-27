import uuid
import os
from flask import Flask,jsonify,request
from flask.views import MethodView
from flask_smorest import Api,Blueprint
from db import db
from models.item_model import ItemModel
from sqlalchemy.exc import SQLAlchemyError
from schema import TagSchema,TagUpdateSchema

blp = Blueprint("Tags","tags", description = "API endpoints for tags collections")

class Tag(MethodView):
    @blp.route("/tags", methods = ['GET'])
    def get_tags():
        pass
    
    @blp.route("/tags/<string:tag_id>", methods = ['GET'])
    def get_tag_by_id(tag_id):
        pass

    @blp.route("/tags", methods = ['POST'])
    @blp.arguments(TagSchema)
    def create_tag(post_data):
        pass

    @blp.route("/tags/<string:tag_id>", methods = ['PUT'])
    @blp.arguments(TagUpdateSchema)
    def update_tag(post_data):
        pass

    @blp.route("/tags/<string:tag_id>", methods = ['DELETE'])
    def delete_tag(tag_id):
        pass
