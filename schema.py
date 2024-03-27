from marshmallow import fields, Schema

class TagSchema(Schema):
    tag_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class TagUpdateSchema(Schema):
    name = fields.Str(required=True)

class StoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    tags = fields.List(fields.Nested(TagSchema()),dump_only=True)

class StoreUpdateSchema(Schema):
    name = fields.Str(required=True)

class ItemSchema(Schema):
    item_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)    

