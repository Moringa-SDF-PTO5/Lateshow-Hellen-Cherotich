from flask import Blueprint, jsonify
from app.models import Episode, Guest, Appearance
from app.serializers import serialize_episode, serialize_guest, serialize_appearance

episodes_bp = Blueprint('episodes', __name__)
guests_bp = Blueprint('guests', __name__)
appearances_bp = Blueprint('appearances', __name__)

@episodes_bp.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    try:
        episode = Episode.query.get_or_404(episode_id)
        serialized_episode = serialize_episode(episode)
        return jsonify(serialized_episode)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@guests_bp.route('/guests/<int:guest_id>', methods=['GET'])
def get_guest(guest_id):
    try:
        guest = Guest.query.get_or_404(guest_id)
        serialized_guest = serialize_guest(guest)
        return jsonify(serialized_guest)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@appearances_bp.route('/appearances/<int:appearance_id>', methods=['GET'])
def get_appearance(appearance_id):
    try:
        appearance = Appearance.query.get_or_404(appearance_id)
        serialized_appearance = serialize_appearance(appearance)
        return jsonify(serialized_appearance)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
