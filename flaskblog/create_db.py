from flaskblog import app, db  # Import your Flask app instance and SQLAlchemy object
from flaskblog import User, Post  # Import your SQLAlchemy models

# Create all database tables
with app.app_context():
    db.drop_all()
    db.create_all()