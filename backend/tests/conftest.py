import pytest
from app import app # Import the app instance directly
from models import db # Import db from models

@pytest.fixture(scope='module')
def test_client():
    # Use the existing app instance
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    with app.app_context():
        db.create_all()  # Create tables
        yield testing_client  # this is where the testing happens!
        db.drop_all()  # Drop tables