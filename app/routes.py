from flask import Blueprint, jsonify
from app.models import Episode, Guest, Appearance
from app.serializers import serialize_episode, serialize_guest, serialize_appearance

episodes_bp = Blueprint('episodes', __name__, url_prefix='/api/episodes')
guests_bp = Blueprint('guests', __name__, url_prefix='/api/guests')
appearances_bp = Blueprint('appearances', __name__, url_prefix='/api/appearances')

@episodes_bp.route('/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    episode = Episode.query.get_or_404(episode_id)
    serialized_episode = serialize_episode(episode)
    return jsonify(serialized_episode)

@guests_bp.route('/<int:guest_id>', methods=['GET'])
def get_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    serialized_guest = serialize_guest(guest)
    return jsonify(serialized_guest)

@appearances_bp.route('/<int:appearance_id>', methods=['GET'])
def get_appearance(appearance_id):
    appearance = Appearance.query.get_or_404(appearance_id)
    serialized_appearance = serialize_appearance(appearance)
    return jsonify(serialized_appearance)
