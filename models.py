from app import db
from sqlalchemy.orm import validates

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    number = db.Column(db.Integer)
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete')

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number
        }

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))

    @validates('rating')
    def validate_rating(self, key, rating):
        assert 1 <= rating <= 5, 'Rating must be between 1 and 5.'
        return rating

    def serialize(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'episode': self.episode.serialize(),
            'guest': self.guest.serialize()
        }
