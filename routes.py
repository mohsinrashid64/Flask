# routes.py
from flask import Blueprint, request, jsonify
from models import db, Item

bp = Blueprint('main', __name__)

@bp.route('/items', methods=['POST'])
def add_item():
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully!'})

@bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    output = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
    return jsonify(output)
