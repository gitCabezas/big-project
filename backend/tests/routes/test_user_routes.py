
import json
import pytest
from services import user_service

# Helper function to get an auth token
def get_auth_header(test_client, username="testuser_routes", email="test_routes@user.com", password="password"):
    try:
        user_service.create_user(username, email, password)
    except Exception:
        # User might already exist, which is fine for this helper
        pass
    
    login_response = test_client.post(
        '/auth/login',
        data=json.dumps({'username': username, 'password': password}),
        content_type='application/json'
    )
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_get_all_users(test_client):
    """Test getting all users requires auth."""
    headers = get_auth_header(test_client)
    response = test_client.get('/api/users/', headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_user_by_id(test_client):
    """Test getting a single user by ID."""
    headers = get_auth_header(test_client)
    # Get the user created by the helper
    user_response = test_client.get('/api/users/', headers=headers)
    user_id = json.loads(user_response.data)[0]['id']

    response = test_client.get(f'/api/users/{user_id}', headers=headers)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == user_id

def test_get_user_unauthorized(test_client):
    """Test that unauthorized access to user routes is forbidden."""
    response = test_client.get('/api/users/')
    assert response.status_code == 401 # Expecting Unauthorized

    response = test_client.get('/api/users/1')
    assert response.status_code == 401
