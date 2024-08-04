# routes.py
from flask import Blueprint, request, jsonify
from models import db, Item

api = Blueprint('main', __name__)

@api.route('/', methods=['GET'])
def api_runnig():
    return {"response":'API Running'}


@api.route('/kinde_hook', methods=['GET'])
def kinde_hook():
    return {"response":'Kinde Hook Executed'}
