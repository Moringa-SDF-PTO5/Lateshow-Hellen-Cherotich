from flask import Blueprint, jsonify, request
from . import db
from .models import Episode, Guest, Appearance
from .serializers import serialize_episode, serialize_guest, serialize_appearance

routes = Blueprint('routes', __name__)

@routes.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([serialize_episode(ep) for ep in episodes])

@routes.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(serialize_episode(episode))
    return jsonify({'error': 'Episode not found'}), 404

@routes.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([serialize_guest(guest) for guest in guests])

@routes.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    if not all([rating, episode_id, guest_id]):
        return jsonify({'errors': ['Missing data']}), 400

    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({'error': 'Invalid episode or guest ID'}), 404

    if rating < 1 or rating > 5:
        return jsonify({'errors': ['Rating must be between 1 and 5']}), 400

    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify(serialize_appearance(appearance)), 201
