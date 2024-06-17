# app/routes.py

from flask import Blueprint, jsonify
from app.models import Episode, Guest, Appearance
from app.serializers import serialize_episode, serialize_guest, serialize_appearance

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    serialized_episodes = [serialize_episode(episode) for episode in episodes]
    return jsonify(serialized_episodes)

@routes_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(serialize_episode(episode))

@routes_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    serialized_guests = [serialize_guest(guest) for guest in guests]
    return jsonify(serialized_guests)

# Add more routes as needed
