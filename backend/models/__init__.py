from flask_sqlalchemy import SQLAlchemy
from app import app # Import app instance from the main app.py

db = SQLAlchemy(app)
