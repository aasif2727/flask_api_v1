import uuid
from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    tag_id = db.Column(db.String(),primary_key=True,default= lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), unique=True, nullable =True)
    store_id = db.Column(db.String(),db.ForeignKey("stores.store_id"), unique=False,nullable=False)

    stores = db.relationship("StoreModel",back_populates="tags")

    def to_dict(self):
        return {'tag_id': self.tag_id,'name': self.name,'store_id':self.store_id}