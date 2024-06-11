from flask import jsonify, request
from app import app, db
from app.models import Episode, Guest, Appearance

@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    serialized_episodes = [episode.serialize() for episode in episodes]
    return jsonify(serialized_episodes)

@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(episode.serialize())

@app.route('/guests')
def get_guests():
    guests = Guest.query.all()
    serialized_guests = [guest.serialize() for guest in guests]
    return jsonify(serialized_guests)

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    if not all([rating, episode_id, guest_id]):
        return jsonify({'errors': ['Missing data']}), 400

    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.serialize()), 201
