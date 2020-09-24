from flask import Blueprint, jsonify

pingPong = Blueprint('pingPong', __name__)

@pingPong.route('/ping')
def ping_pong():
    return jsonify({'message':'pong'})