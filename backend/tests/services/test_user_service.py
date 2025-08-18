import pytest
from services import user_service
from models.user_model import User, db

# The test_client fixture from conftest.py will handle db setup/teardown
# and provide an app context.

def test_create_user(test_client):
    """Test creating a new user."""
    username = "testuser"
    email = "test@example.com"
    password = "password123"
    user = user_service.create_user(username, email, password)

    assert user is not None
    assert user.username == username
    assert user.email == email
    assert user.id is not None

    # Verify user exists in the database
    retrieved_user = User.query.filter_by(username=username).first()
    assert retrieved_user is not None
    assert retrieved_user.email == email

def test_create_user_duplicate_username(test_client):
    """Test creating a user with a duplicate username."""
    username = "duplicateuser"
    email1 = "duplicate1@example.com"
    email2 = "duplicate2@example.com"
    password = "password123"

    user_service.create_user(username, email1, password)

    # Attempt to create another user with the same username
    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        user_service.create_user(username, email2, password)

def test_get_all_users(test_client):
    """Test retrieving all users."""
    user_service.create_user("user1", "user1@example.com", "pass1")
    user_service.create_user("user2", "user2@example.com", "pass2")
    users = user_service.get_all_users()
    assert len(users) >= 2 # Account for potential users from other tests if db isn't fully cleared

def test_get_user_by_id(test_client):
    """Test retrieving a user by ID."""
    username = "user_by_id"
    email = "id@example.com"
    password = "password123"
    created_user = user_service.create_user(username, email, password)

    retrieved_user = user_service.get_user_by_id(created_user.id)
    assert retrieved_user is not None
    assert retrieved_user.username == username
    assert retrieved_user.email == email

def test_get_user_by_id_non_existent(test_client):
    """Test retrieving a non-existent user by ID."""
    retrieved_user = user_service.get_user_by_id(99999) # Assuming this ID does not exist
    assert retrieved_user is None

def test_update_user(test_client):
    """Test updating an existing user."""
    username = "oldname"
    email = "old@example.com"
    password = "oldpass"
    user = user_service.create_user(username, email, password)

    updated_data = {
        "username": "newname",
        "email": "new@example.com",
        "password": "newpass"
    }
    updated_user = user_service.update_user(user.id, updated_data)

    assert updated_user is not None
    assert updated_user.username == "newname"
    assert updated_user.email == "new@example.com"
    # Password hash is updated, but we don't check it directly here.
    # A separate test for check_password would be good.

    # Verify changes in DB
    retrieved_user = User.query.get(user.id)
    assert retrieved_user.username == "newname"
    assert retrieved_user.email == "new@example.com"

def test_update_user_non_existent(test_client):
    """Test updating a non-existent user."""
    updated_user = user_service.update_user(99999, {"username": "nonexistent"})
    assert updated_user is None

def test_delete_user(test_client):
    """Test deleting an existing user."""
    username = "todelete"
    email = "delete@example.com"
    password = "password123"
    user = user_service.create_user(username, email, password)

    result = user_service.delete_user(user.id)
    assert result is True

    # Verify user is deleted from DB
    retrieved_user = User.query.get(user.id)
    assert retrieved_user is None

def test_delete_user_non_existent(test_client):
    """Test deleting a non-existent user."""
    result = user_service.delete_user(99999)
    assert result is False