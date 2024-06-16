def serialize_episode(episode):
    return {
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': [serialize_appearance(app) for app in episode.appearances]
    }

def serialize_guest(guest):
    return {
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation,
        'appearances': [serialize_appearance(app) for app in guest.appearances]
    }

def serialize_appearance(appearance):
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'episode_id': appearance.episode_id,
        'guest_id': appearance.guest_id,
        'episode': {
            'id': appearance.episode.id,
            'date': appearance.episode.date,
            'number': appearance.episode.number
        },
        'guest': {
            'id': appearance.guest.id,
            'name': appearance.guest.name,
            'occupation': appearance.guest.occupation
        }
    }
