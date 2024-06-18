def serialize_episode(episode):
    return {
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': [serialize_appearance_light(appearance) for appearance in episode.appearances]
    }

def serialize_guest(guest):
    return {
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation,
        'appearances': [serialize_appearance_light(appearance) for appearance in guest.appearances]
    }

def serialize_appearance_light(appearance):
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'episode_id': appearance.episode_id,
        'guest_id': appearance.guest_id
    }

def serialize_appearance(appearance):
    return {
        'id': appearance.id,
        'rating': appearance.rating,
        'episode': serialize_episode_light(appearance.episode),
        'guest': serialize_guest_light(appearance.guest)
    }

def serialize_episode_light(episode):
    return {
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
    }

def serialize_guest_light(guest):
    return {
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation,
    }
