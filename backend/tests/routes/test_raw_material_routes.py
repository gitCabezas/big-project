
import json
import pytest
from services import user_service

# Helper function to get an auth token
def get_auth_header(test_client, username="rm_user", email="rm@user.com", password="password"):
    try:
        user_service.create_user(username, email, password)
    except Exception:
        pass
    login_response = test_client.post('/auth/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_raw_material_crud(test_client):
    headers = get_auth_header(test_client)
    
    # Create
    response = test_client.post('/api/raw_materials/', headers=headers, data=json.dumps({'name': 'Silk', 'type': 'Natural'}), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    rm_id = data['id']

    # Read
    response = test_client.get(f'/api/raw_materials/{rm_id}', headers=headers)
    assert response.status_code == 200
    assert json.loads(response.data)['name'] == 'Silk'

    # Update
    response = test_client.put(f'/api/raw_materials/{rm_id}', headers=headers, data=json.dumps({'name': 'Fine Silk', 'unit_of_measure': 'M'}), content_type='application/json')
    assert response.status_code == 200

    # Delete
    response = test_client.delete(f'/api/raw_materials/{rm_id}', headers=headers)
    assert response.status_code == 204
