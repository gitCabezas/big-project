
import json
import pytest
from services import user_service, client_service, color_service, raw_material_service, dye_service, chemical_input_service

# Helper function to get an auth token
def get_auth_header(test_client, username="recipe_user", email="recipe@user.com", password="password"):
    try:
        user_service.create_user(username, email, password)
    except Exception:
        pass
    login_response = test_client.post('/auth/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    token = json.loads(login_response.data)['token']
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture(scope="function")
def setup_dependencies(test_client):
    """Fixture to create necessary items for recipe tests."""
    client = client_service.create_client({"name": "Recipe Test Client", "cnpj_cpf": "00000000000000"})
    color = color_service.create_color({"name": "Recipe Test Color"})
    raw_material = raw_material_service.create_raw_material({"name": "Recipe Test Material", "type": "Test Type"})
    dye = dye_service.create_dye({"commercial_name": "Recipe Test Dye", "code": "RTD-01"})
    chemical = chemical_input_service.create_chemical_input({"name": "Recipe Test Chemical"})
    return {"client_id": client['id'], "color_id": color['id'], "raw_material_id": raw_material['id'], "dye_id": dye['id'], "chemical_id": chemical['id']}

def test_recipe_crud(test_client, setup_dependencies):
    headers = get_auth_header(test_client)
    deps = setup_dependencies

    # Create
    payload = {
        "name": "REC-001",
        "client_id": deps["client_id"],
        "color_id": deps["color_id"],
        "raw_material_id": deps["raw_material_id"],
        "dyes": [{"dye_id": deps["dye_id"], "quantity": 1.5}],
        "chemical_inputs": [{"chemical_input_id": deps["chemical_id"], "quantity": 10.0}]
    }
    response = test_client.post('/api/recipes/', headers=headers, data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    recipe_id = data['id']

    # Read
    response = test_client.get(f'/api/recipes/{recipe_id}', headers=headers)
    assert response.status_code == 200
    retrieved_data = json.loads(response.data)
    assert retrieved_data['name'] == 'REC-001'
    assert len(retrieved_data['dyes']) == 1

    # Delete
    response = test_client.delete(f'/api/recipes/{recipe_id}', headers=headers)
    assert response.status_code == 204
