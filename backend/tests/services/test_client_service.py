import pytest
from services import client_service
from models.client_model import Client, db

def test_create_client(test_client):
    """Test creating a new client."""
    client_data = {
        "name": "Test Client",
        "cnpj_cpf": "12.345.678/0001-90",
        "address": "Test Address, 123",
        "contact": "test@example.com",
        "observations": "Some observations"
    }
    client_dict = client_service.create_client(client_data)

    assert client_dict is not None
    assert client_dict['name'] == client_data['name']
    assert client_dict['cnpj_cpf'] == client_data['cnpj_cpf']
    assert client_dict['is_active'] is True

    # Verify client exists in the database
    retrieved_client = Client.query.filter_by(cnpj_cpf=client_data['cnpj_cpf']).first()
    assert retrieved_client is not None
    assert retrieved_client.name == client_data['name']

def test_create_client_duplicate_cnpj_cpf(test_client):
    """Test creating a client with a duplicate CNPJ/CPF."""
    client_data1 = {
        "name": "Client A",
        "cnpj_cpf": "11.111.111/0001-11",
    }
    client_data2 = {
        "name": "Client B",
        "cnpj_cpf": "11.111.111/0001-11",
    }
    client_service.create_client(client_data1)

    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        client_service.create_client(client_data2)

def test_get_all_clients(test_client):
    """Test retrieving all active clients."""
    client_service.create_client({"name": "Active Client 1", "cnpj_cpf": "22.222.222/0001-22"})
    client_service.create_client({"name": "Active Client 2", "cnpj_cpf": "33.333.333/0001-33"})
    
    # Create a deactivated client to ensure it's not returned by get_all_clients
    deactivated_client_data = {"name": "Deactivated Client", "cnpj_cpf": "44.444.444/0001-44"}
    deactivated_client_dict = client_service.create_client(deactivated_client_data)
    client_service.deactivate_client(deactivated_client_dict['id'])

    clients = client_service.get_all_clients()
    # Assert that at least 2 active clients are returned (depending on test order)
    # and the deactivated client is not in the list
    assert len(clients) >= 2
    assert not any(c['cnpj_cpf'] == deactivated_client_data['cnpj_cpf'] for c in clients)


def test_get_client_by_id(test_client):
    """Test retrieving a client by ID."""
    client_data = {
        "name": "Client By ID",
        "cnpj_cpf": "55.555.555/0001-55",
    }
    created_client_dict = client_service.create_client(client_data)

    retrieved_client_dict = client_service.get_client_by_id(created_client_dict['id'])
    assert retrieved_client_dict is not None
    assert retrieved_client_dict['name'] == client_data['name']
    assert retrieved_client_dict['cnpj_cpf'] == client_data['cnpj_cpf']

def test_get_client_by_id_non_existent(test_client):
    """Test retrieving a non-existent client by ID."""
    retrieved_client = client_service.get_client_by_id(99999) # Assuming this ID does not exist
    assert retrieved_client is None

def test_update_client(test_client):
    """Test updating an existing client."""
    client_data = {
        "name": "Old Client Name",
        "cnpj_cpf": "66.666.666/0001-66",
        "address": "Old Address"
    }
    client_dict = client_service.create_client(client_data)

    updated_data = {
        "name": "New Client Name",
        "address": "New Address",
        "contact": "new@example.com"
    }
    updated_client_dict = client_service.update_client(client_dict['id'], updated_data)

    assert updated_client_dict is not None
    assert updated_client_dict['name'] == updated_data['name']
    assert updated_client_dict['address'] == updated_data['address']
    assert updated_client_dict['contact'] == updated_data['contact']
    assert updated_client_dict['cnpj_cpf'] == client_data['cnpj_cpf'] # CNPJ/CPF should remain unchanged

    # Verify changes in DB
    retrieved_client = Client.query.get(client_dict['id'])
    assert retrieved_client.name == updated_data['name']
    assert retrieved_client.address == updated_data['address']

def test_update_client_non_existent(test_client):
    """Test updating a non-existent client."""
    updated_client = client_service.update_client(99999, {"name": "nonexistent"})
    assert updated_client is None

def test_deactivate_client(test_client):
    """Test deactivating an existing client."""
    client_data = {
        "name": "To Deactivate",
        "cnpj_cpf": "77.777.777/0001-77",
    }
    client_dict = client_service.create_client(client_data)

    deactivated_client_dict = client_service.deactivate_client(client_dict['id'])
    assert deactivated_client_dict is not None
    assert deactivated_client_dict['is_active'] is False

    # Verify client is deactivated in DB
    retrieved_client = Client.query.get(client_dict['id'])
    assert retrieved_client.is_active is False

    # Ensure deactivated client is not returned by get_all_clients
    clients = client_service.get_all_clients()
    assert not any(c['id'] == client_dict['id'] for c in clients)

def test_deactivate_client_non_existent(test_client):
    """Test deactivating a non-existent client."""
    result = client_service.deactivate_client(99999)
    assert result is None