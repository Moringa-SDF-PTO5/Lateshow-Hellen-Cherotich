from app import create_app, db
from app.models import Episode, Guest, Appearance

app = create_app()

with app.app_context():
    # Drop all tables and create them again
    db.drop_all()
    db.create_all()

    # Create sample data
    episode1 = Episode(date='2023-06-18', number=1)
    episode2 = Episode(date='2023-06-19', number=2)

    guest1 = Guest(name='John Doe', occupation='Actor')
    guest2 = Guest(name='Jane Smith', occupation='Musician')

    appearance1 = Appearance(rating=5, episode=episode1, guest=guest1)
    appearance2 = Appearance(rating=4, episode=episode2, guest=guest2)

    # Add the data to the session and commit it
    db.session.add_all([episode1, episode2, guest1, guest2, appearance1, appearance2])
    db.session.commit()

    print('Database seeded successfully.')
