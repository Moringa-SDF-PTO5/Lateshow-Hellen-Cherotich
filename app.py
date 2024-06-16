import csv
from . import db
from .models import Episode, Guest, Appearance
from . import create_app

def seed_data():
    app = create_app()
    with app.app_context():
        with open('seed_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['type'] == 'episode':
                    episode = Episode(id=row['id'], date=row['date'], number=row['number'])
                    db.session.add(episode)
                elif row['type'] == 'guest':
                    guest = Guest(id=row['id'], name=row['name'], occupation=row['occupation'])
                    db.session.add(guest)
                elif row['type'] == 'appearance':
                    appearance = Appearance(rating=row['rating'], episode_id=row['episode_id'], guest_id=row['guest_id'])
                    db.session.add(appearance)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
