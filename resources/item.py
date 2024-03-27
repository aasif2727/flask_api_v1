import os
import uuid
from flask import Flask, jsonify, request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from sqlalchemy.exc import SQLAlchemyError
from schema import ItemSchema, ItemUpdateSchema
from models.item_model import ItemModel


blp = Blueprint("Items","items",description = "API endpoints for Items collections")

class Item(MethodView):
    
    @blp.route("/items", methods = ['GET'])
    def get_items():
        try:
            items = ItemModel.query.all()
            item_list = [item.to_dict() for item in items]
            if item_list:
                return jsonify(item_list)
            else:
                return jsonify([])
        except KeyError as ex:
            abort(500, message= f"Invalid request. Exception - {ex}")

    @blp.route("/items/<string:item_id>", methods = ['GET'])
    def get_item_by_id(item_id):
        try:
            item = ItemModel.query.filter_by(item_id=item_id).first_or_404()
            return jsonify(item.to_dict())
        except SQLAlchemyError as ex:
            return {"message": "DB error occurred - {0}".format(ex._sql_message)}, 400
        except:
            abort(404, message = f"Item-{item_id} not found.")

    @blp.route("/items", methods = ['POST'])
    @blp.arguments(ItemSchema)
    def create_item(post_data):
        try:
            # post_data = request.get_json()
            #new_item = {"item_id": uuid.uuid4().hex, "name" : post_data["name"]}
            #items.append(new_item)
            item = ItemModel(**post_data) #converts the request dictionary object to db model object
            db.session.add(item)
            db.session.commit()
            return {"message": "Item created successfully."}, 200      
        except SQLAlchemyError as ex:
            return {"message": "DB error occurred - {0}".format(ex._sql_message)}, 400
        except:
            abort(404, message = f"Item creation failed.")

    @blp.route("/items/<string:item_id>", methods = ['PUT'])
    @blp.arguments(ItemUpdateSchema)
    def update_item(update_data,item_id):
        try:
            item = ItemModel.query.get_or_404(item_id)
            for key,value in update_data:
                setattr(item,key,value)
            db.session.commit()
            return {"message": "Item updated successfully."}, 200
        except:
            abort(404, message = f"Update failed for Item-{item_id}.")
    
    @blp.route("/items/<string:item_id>", methods = ['DELETE'])
    def delete_item(item_id):
        try:
            item = ItemModel.query.get_or_404(item_id)
            db.session.delete(item)
            db.session.commit()
            return {"message": "Item deleted successfully."}, 200
        except:
            abort(404, message = f"Item-{item_id} not found.")