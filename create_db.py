from flaskblog import app, db  # Import your Flask app instance and SQLAlchemy object
from flaskblog.models import User, Post  # Import your SQLAlchemy models

# Create all database tables
with app.app_context():
    posts = Post.query.paginate()
    print(posts.total)