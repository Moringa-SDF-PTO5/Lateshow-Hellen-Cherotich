from . import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete')

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete')

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    __table_args__ = (db.CheckConstraint('rating >= 1 AND rating <= 5', name='rating_between_1_and_5'),)
