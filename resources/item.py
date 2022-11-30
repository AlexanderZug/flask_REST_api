import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint('Items', 'items', description='Operations on items')


@blp.route('/items/<string:item_id>')
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, massage='Item not found')

    def delete(self, item_id):
        try:
            del items[item_id]
            return {'massage': 'Item deleted'}
        except KeyError:
            abort(404, massage='Item not found')

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, massage='Item not found')


@blp.route('/items')
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        if item_data['store_id'] not in stores:
            abort(404, massage='Store not found')

        item_id = uuid.uuid4().hex
        item = {**item_data, 'id': item_id}
        items[item_id] = item
        return item, 201