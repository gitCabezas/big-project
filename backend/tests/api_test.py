import json
from services.user_service import create_user

# Helper function to get an auth token
def get_auth_header(test_client, username="api_test_user", email="apitest@user.com", password="password"):
    try:
        create_user(username, email, password)
    except Exception:
        pass
    
    login_response = test_client.post(
        '/auth/login',
        data=json.dumps({'username': username, 'password': password}),
        content_type='application/json'
    )
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_create_user_api(test_client):
    """Test creating a user via the API endpoint."""
    headers = get_auth_header(test_client) # Need to be authenticated to create users
    
    user_data = {
        "username": "RodrigoTesteAPI",
        "email": "rodrigoteste_api@gmail.com",
        "password": "ligo3101"
    }

    response = test_client.post(
        '/api/users/',
        headers=headers,
        data=json.dumps(user_data),
        content_type='application/json'
    )

    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['username'] == "RodrigoTesteAPI"
    assert data['email'] == "rodrigoteste_api@gmail.com"
    assert 'id' in data