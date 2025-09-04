
import json
import pytest
from services import user_service

# Helper function to get an auth token
def get_auth_header(test_client, username="chem_user", email="chem@user.com", password="password"):
    try:
        user_service.create_user(username, email, password)
    except Exception:
        pass
    login_response = test_client.post('/auth/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

def test_chemical_input_crud(test_client):
    headers = get_auth_header(test_client)
    
    # Create
    payload = {'name': 'Acetic Acid', 'unit': 'mL', 'price_per_unit': 15.0}
    response = test_client.post('/api/chemical_inputs/', headers=headers, data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    chem_id = data['id']

    # Read
    response = test_client.get(f'/api/chemical_inputs/{chem_id}', headers=headers)
    assert response.status_code == 200

    # Update
    update_payload = {'price_per_unit': 17.5}
    response = test_client.put(f'/api/chemical_inputs/{chem_id}', headers=headers, data=json.dumps(update_payload), content_type='application/json')
    assert response.status_code == 200

    # Delete
    response = test_client.delete(f'/api/chemical_inputs/{chem_id}', headers=headers)
    assert response.status_code == 204
