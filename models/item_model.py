import uuid
from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    item_id = db.Column(db.String(),primary_key = True,default = lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), unique=True, nullable =True)
    price = db.Column(db.Float(precision=2), nullable =False)
    store_id = db.Column(db.String(),db.ForeignKey("stores.store_id"), unique=False,nullable=False)

    def to_dict(self):
        return {'id': self.item_id,'name': self.name,'price':self.price,'store_id':self.store_id}