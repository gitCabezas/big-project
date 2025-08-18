import pytest
from services import chemical_input_service
from models.chemical_input_model import ChemicalInput, db
from datetime import datetime

def test_create_chemical_input(test_client):
    """Test creating a new chemical input."""
    input_data = {
        "name": "Ácido Acético",
        "function": "Neutralizante",
        "supplier": "Fornecedor Químico",
        "concentration": 99.0,
        "safety_data_sheet_url": "http://example.com/sds/acido_acetico.pdf",
        "validity": datetime(2025, 12, 31),
        "stock_quantity": 500.0
    }
    input_dict = chemical_input_service.create_chemical_input(input_data)

    assert input_dict is not None
    assert input_dict['name'] == input_data['name']
    assert input_dict['function'] == input_data['function']
    assert input_dict['stock_quantity'] == input_data['stock_quantity']
    assert input_dict['validity'] == input_data['validity'].isoformat()

    # Verify input exists in the database
    retrieved_input = ChemicalInput.query.filter_by(name=input_data['name']).first()
    assert retrieved_input is not None
    assert retrieved_input.function == input_data['function']

def test_create_chemical_input_duplicate_name(test_client):
    """Test creating a chemical input with a duplicate name."""
    input_data1 = {
        "name": "Químico Duplicado",
        "function": "Auxiliar",
    }
    input_data2 = {
        "name": "Químico Duplicado",
        "function": "Fixador",
    }
    chemical_input_service.create_chemical_input(input_data1)

    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        chemical_input_service.create_chemical_input(input_data2)

def test_get_all_chemical_inputs(test_client):
    """Test retrieving all chemical inputs."""
    chemical_input_service.create_chemical_input({"name": "Input A", "function": "Auxiliar"})
    chemical_input_service.create_chemical_input({"name": "Input B", "function": "Fixador"})
    inputs = chemical_input_service.get_all_chemical_inputs()
    assert len(inputs) >= 2

def test_get_chemical_input_by_id(test_client):
    """Test retrieving a chemical input by ID."""
    input_data = {
        "name": "Input By ID",
        "function": "Auxiliar",
    }
    created_input_dict = chemical_input_service.create_chemical_input(input_data)

    retrieved_input_dict = chemical_input_service.get_chemical_input_by_id(created_input_dict['id'])
    assert retrieved_input_dict is not None
    assert retrieved_input_dict['name'] == input_data['name']
    assert retrieved_input_dict['function'] == input_data['function']

def test_get_chemical_input_by_id_non_existent(test_client):
    """Test retrieving a non-existent chemical input by ID."""
    retrieved_input = chemical_input_service.get_chemical_input_by_id(99999)
    assert retrieved_input is None

def test_update_chemical_input(test_client):
    """Test updating an existing chemical input."""
    input_data = {
        "name": "Old Chemical",
        "function": "Old Function",
        "stock_quantity": 100.0
    }
    input_dict = chemical_input_service.create_chemical_input(input_data)

    updated_data = {
        "name": "New Chemical Name",
        "function": "New Function",
        "concentration": 75.0,
        "stock_quantity": 200.0,
        "validity": datetime(2026, 1, 1)
    }
    updated_input_dict = chemical_input_service.update_chemical_input(input_dict['id'], updated_data)

    assert updated_input_dict is not None
    assert updated_input_dict['name'] == updated_data['name']
    assert updated_input_dict['function'] == updated_data['function']
    assert updated_input_dict['concentration'] == updated_data['concentration']
    assert updated_input_dict['stock_quantity'] == updated_data['stock_quantity']
    assert updated_input_dict['validity'] == updated_data['validity'].isoformat()

    # Verify changes in DB
    retrieved_input = ChemicalInput.query.get(input_dict['id'])
    assert retrieved_input.name == updated_data['name']
    assert retrieved_input.function == updated_data['function']

def test_update_chemical_input_non_existent(test_client):
    """Test updating a non-existent chemical input."""
    updated_input = chemical_input_service.update_chemical_input(99999, {"name": "nonexistent"})
    assert updated_input is None

def test_delete_chemical_input(test_client):
    """Test deleting an existing chemical input."""
    input_data = {
        "name": "To Delete Chemical",
        "function": "Auxiliar",
    }
    input_dict = chemical_input_service.create_chemical_input(input_data)

    result = chemical_input_service.delete_chemical_input(input_dict['id'])
    assert result is True

    # Verify input is deleted from DB
    retrieved_input = ChemicalInput.query.get(input_dict['id'])
    assert retrieved_input is None

def test_delete_chemical_input_non_existent(test_client):
    """Test deleting a non-existent chemical input."""
    result = chemical_input_service.delete_chemical_input(99999)
    assert result is False