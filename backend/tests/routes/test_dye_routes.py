
import json
import pytest
from services import user_service

# Helper function to get an auth token
def get_auth_header(test_client, username="dye_user", email="dye@user.com", password="password"):
    try:
        user_service.create_user(username, email, password)
    except Exception:
        pass
    login_response = test_client.post('/auth/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_dye_crud(test_client):
    headers = get_auth_header(test_client)
    
    # Create
    payload = {'commercial_name': 'Indigo', 'code': 'IND-01'}
    response = test_client.post('/api/dyes/', headers=headers, data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    dye_id = data['id']

    # Read
    response = test_client.get(f'/api/dyes/{dye_id}', headers=headers)
    assert response.status_code == 200
    assert json.loads(response.data)['commercial_name'] == 'Indigo'

    # Update
    update_payload = {'name': 'Deep Indigo', 'price_per_kg': 275.5}
    response = test_client.put(f'/api/dyes/{dye_id}', headers=headers, data=json.dumps(update_payload), content_type='application/json')
    assert response.status_code == 200

    # Delete
    response = test_client.delete(f'/api/dyes/{dye_id}', headers=headers)
    assert response.status_code == 204
