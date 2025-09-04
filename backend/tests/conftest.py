import pytest
from app import app, db

@pytest.fixture(scope='function') # Changed scope to function
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()

    with flask_app.app_context():
        db.create_all()  # Create tables for each test function
        yield testing_client
        db.session.remove() # Clean up the session
        db.drop_all()  # Drop tables after each test function