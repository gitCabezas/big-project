
import json
import pytest
from services import user_service, client_service

# Helper function to get an auth token
def get_auth_header(test_client, username="client_user", email="client@user.com", password="password"):
    try:
        user_service.create_user(username, email, password)
    except Exception:
        pass
    login_response = test_client.post('/auth/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_client_crud_operations(test_client):
    headers = get_auth_header(test_client)

    # 1. Create Client
    create_response = test_client.post('/api/clients/', headers=headers, data=json.dumps({'name': 'New Client', 'cnpj_cpf': '12345678901234'}), content_type='application/json')
    assert create_response.status_code == 201
    client_data = json.loads(create_response.data)
    client_id = client_data['id']
    assert client_data['name'] == 'New Client'

    # 2. Get All Clients
    get_all_response = test_client.get('/api/clients/', headers=headers)
    assert get_all_response.status_code == 200
    assert isinstance(json.loads(get_all_response.data), list)

    # 3. Get Client by ID
    get_one_response = test_client.get(f'/api/clients/{client_id}', headers=headers)
    assert get_one_response.status_code == 200
    assert json.loads(get_one_response.data)['id'] == client_id

    # 4. Update Client
    update_response = test_client.put(f'/api/clients/{client_id}', headers=headers, data=json.dumps({'name': 'Updated Client'}), content_type='application/json')
    assert update_response.status_code == 200
    assert json.loads(update_response.data)['name'] == 'Updated Client'

    # 5. Delete Client
    delete_response = test_client.delete(f'/api/clients/{client_id}', headers=headers)
    assert delete_response.status_code == 204

    # Verify deletion
    get_deleted_response = test_client.get(f'/api/clients/{client_id}', headers=headers)
    assert get_deleted_response.status_code == 404

def test_client_routes_unauthorized(test_client):
    """Test that client routes are protected."""
    response = test_client.get('/api/clients/')
    assert response.status_code == 401

    response = test_client.get('/api/clients/1')
    assert response.status_code == 401

    response = test_client.post('/api/clients/', data=json.dumps({'name': 'test', 'cnpj_cpf': '123'}), content_type='application/json')
    assert response.status_code == 401

    response = test_client.put('/api/clients/1', data=json.dumps({'name': 'test'}), content_type='application/json')
    assert response.status_code == 401

    response = test_client.delete('/api/clients/1')
    assert response.status_code == 401

    response = test_client.put('/api/clients/1/deactivate')
    assert response.status_code == 401

def test_create_client_missing_fields(test_client):
    """Test creating a client with missing required fields."""
    headers = get_auth_header(test_client, username="client_user_2", email="client2@user.com")

    # Test with empty payload
    response = test_client.post('/api/clients/', headers=headers, data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'Input payload validation failed' in data['message']

    # Test with only cnpj_cpf (name is required)
    response = test_client.post('/api/clients/', headers=headers, data=json.dumps({'cnpj_cpf': '12345678901234'}), content_type='application/json')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'Input payload validation failed' in data['message']
