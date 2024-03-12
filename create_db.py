from flaskblog import app, db  # Import your Flask app instance and SQLAlchemy object
from flaskblog.models import User, Post  # Import your SQLAlchemy models

# Create all database tables
with app.app_context():
    users = User.query.all()
    for user in users:
        print(user)