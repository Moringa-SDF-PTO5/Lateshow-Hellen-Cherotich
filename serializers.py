def serialize_episode(episode):
    return {
        'id': episode.id,
        'date': episode.date,
        'number': episode.number
    }

def serialize_guest(guest):
    return {
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    }

def serialize_appearance(appearance):
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'episode': serialize_episode(appearance.episode),
        'guest': serialize_guest(appearance.guest)
    }
