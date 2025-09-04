import json

def test_login_success(test_client):
    """Test successful user login."""
    from services.user_service import create_user
    # Create the user first so login can succeed
    try:
        create_user(
            username='textilandina@uol.com.br',
            email='textilandina@uol.com.br',
            password='270271'
        )
    except Exception:
        pass # User might already exist from a previous failed run

    response = test_client.post(
        '/auth/login',
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
        '/auth/login',
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
        '/auth/login',
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
    # Test with missing password
    response = test_client.post(
        '/auth/login',
        data=json.dumps({'username': 'test@example.com'}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Input payload validation failed'

    # Test with missing username
    response = test_client.post(
        '/auth/login',
        data=json.dumps({'password': 'password123'}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Input payload validation failed'

    # Test with both missing
    response = test_client.post(
        '/auth/login',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['message'] == 'Input payload validation failed'