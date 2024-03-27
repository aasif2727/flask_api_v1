import uuid
from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), unique=True, nullable =True)
    #tags = db.relationship("TagModel",back_populates="stores",lazy="dynamic")
    
    def to_dict(self):
        return {'store_id': self.store_id,'name': self.name}