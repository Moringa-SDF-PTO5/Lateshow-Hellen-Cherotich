# app/serializers.py

def serialize_episode(episode):
    return {
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': [
            {
                'id': app.id,
                'rating': app.rating,
                'episode_id': app.episode_id,
                'guest_id': app.guest_id,
                'guest': serialize_guest(app.guest)
            } for app in episode.appearances
        ]
    }

def serialize_guest(guest):
    return {
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation,
        'appearances': [
            {
                'id': app.id,
                'rating': app.rating,
                'episode_id': app.episode_id,
                'guest_id': app.guest_id,
                'episode': serialize_episode(app.episode)
            } for app in guest.appearances
        ]
    }

def serialize_appearance(appearance):
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'episode_id': appearance.episode_id,
        'guest_id': appearance.guest_id,
        'episode': serialize_episode(appearance.episode),
        'guest': serialize_guest(appearance.guest)
    }
