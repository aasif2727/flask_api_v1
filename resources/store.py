import os
import uuid
from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from schema import StoreSchema, StoreUpdateSchema
from models.store_model import StoreModel
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Stores","stores", description = "API endpoints for stores collections")

class Store(MethodView):
    @blp.route("/stores", methods=['GET'])
    def get_stores():
        try:
            stores = StoreModel.query.all()
            stores_list = [store.to_dict() for store in stores]  # Convert SQLAlchemy instances to dictionaries
            if stores_list:
                return jsonify(stores_list)
            else:
                return {"message": "No stores found."}, 201
        except KeyError as ex:
            abort(500, message= "Invalid request - {0}".format(ex))

    @blp.route("/stores", methods=['POST'])
    @blp.arguments(StoreSchema)
    def post_store(post_data):
        try:
            #post_data = request.get_json()
            #new_store = {"store_id": uuid.uuid4().hex, "name" : post_data["name"], "items" : []}
            #store_id = uuid.uuid4().hex

            store = StoreModel(**post_data) #converts the request dictionary object to db model object
            db.session.add(store)
            db.session.commit()
            return {"message": "Store created successfully."}, 200      
        except SQLAlchemyError as ex:
            return {"message": "DB error occurred - {0}".format(ex._sql_message)}, 400
        except KeyError as ex:
            abort(500, message = f"Store creation failed - {ex}")

    @blp.route("/stores/<string:store_id>",methods=['GET'])  
    def get_store_by_id(store_id):
        try:
            store = StoreModel.query.filter_by(store_id=store_id).first()
            return jsonify(store.to_dict())
        except KeyError as ex:
            abort(404, message = f"store-{store_id} not found. Exception : {ex}")

    @blp.route("/stores/<string:store_id>",methods=['PUT'])  
    @blp.arguments(StoreUpdateSchema)
    def update_store(update_data,store_id):
        try:
            store = StoreModel.query.get_or_404(store_id)
            for key, value in update_data.items():
                setattr(store, key, value)
            db.session.commit() 
            return {"message": "Store updated successfully."}, 200
        except:
            abort(404, message = f"Update failed for Store-{store_id}.")

    @blp.route("/stores/<string:store_id>",methods=['DELETE'])
    def delete_store(store_id):
        try:
            store = StoreModel.query.get_or_404(store_id)
            db.session.delete(store)  # Delete the object using SQLAlchemy
            db.session.commit()
            return {"message": "Store deleted successfully."}, 200
        except KeyError as ex:
            abort(404, message = f"store-{store_id} not found.Exception : {ex}")