import json

def test_login_success(test_client):
    """Test successful user login."""
    response = test_client.post(
        '/api/auth/login',
        data=json.dumps({
            'username': 'textilandina@uol.com.br',
            'password': '270271'
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'token' in data
    assert data['message'] == 'Login successful'

def test_login_invalid_credentials(test_client):
    """Test login with invalid password."""
    response = test_client.post(
        '/api/auth/login',
        data=json.dumps({
            'username': 'textilandina@uol.com.br',
            'password': 'wrong_password'
        }),
        content_type='application/json'
    )
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'

def test_login_non_existent_user(test_client):
    """Test login with a non-existent username."""
    response = test_client.post(
        '/api/auth/login',
        data=json.dumps({
            'username': 'nonexistent@example.com',
            'password': 'any_password'
        }),
        content_type='application/json'
    )
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['message'] == 'Invalid credentials'

def test_login_missing_credentials(test_client):
    """Test login with missing username or password."""
    response = test_client.post(
        '/api/auth/login',
        data=json.dumps({
            'username': 'test@example.com'
            # password is missing
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Username and password are required'

    response = test_client.post(
        '/api/auth/login',
        data=json.dumps({
            # username is missing
            'password': 'password123'
        }),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Username and password are required'

    response = test_client.post(
        '/api/auth/login',
        data=json.dumps({}), # both missing
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Username and password are required'