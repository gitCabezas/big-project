import pytest
from services import dye_service
from models.dye_model import Dye, db
from datetime import datetime

def test_create_dye(test_client):
    """Test creating a new dye."""
    dye_data = {
        "commercial_name": "Corante Azul Teste",
        "code": "AZL-001",
        "manufacturer": "Fabricante Teste",
        "type": "Reativo",
        "concentration": 50.0,
        "validity": datetime(2026, 12, 31),
        "stock_quantity": 150.0,
        "lot_number": "LT-AZL-001"
    }
    dye_dict = dye_service.create_dye(dye_data)

    assert dye_dict is not None
    assert dye_dict['commercial_name'] == dye_data['commercial_name']
    assert dye_dict['code'] == dye_data['code']
    assert dye_dict['stock_quantity'] == dye_data['stock_quantity']
    assert dye_dict['validity'] == dye_data['validity'].isoformat() # Check isoformat for datetime

    # Verify dye exists in the database
    retrieved_dye = Dye.query.filter_by(code=dye_data['code']).first()
    assert retrieved_dye is not None
    assert retrieved_dye.commercial_name == dye_data['commercial_name']

def test_create_dye_duplicate_code(test_client):
    """Test creating a dye with a duplicate code."""
    dye_data1 = {
        "commercial_name": "Corante Duplicado A",
        "code": "DUP-001",
    }
    dye_data2 = {
        "commercial_name": "Corante Duplicado B",
        "code": "DUP-001",
    }
    dye_service.create_dye(dye_data1)

    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        dye_service.create_dye(dye_data2)

def test_get_all_dyes(test_client):
    """Test retrieving all dyes."""
    dye_service.create_dye({"commercial_name": "Dye A", "code": "DYE-A"})
    dye_service.create_dye({"commercial_name": "Dye B", "code": "DYE-B"})
    dyes = dye_service.get_all_dyes()
    assert len(dyes) >= 2

def test_get_dye_by_id(test_client):
    """Test retrieving a dye by ID."""
    dye_data = {
        "commercial_name": "Dye By ID",
        "code": "DYE-ID",
    }
    created_dye_dict = dye_service.create_dye(dye_data)

    retrieved_dye_dict = dye_service.get_dye_by_id(created_dye_dict['id'])
    assert retrieved_dye_dict is not None
    assert retrieved_dye_dict['commercial_name'] == dye_data['commercial_name']
    assert retrieved_dye_dict['code'] == dye_data['code']

def test_get_dye_by_id_non_existent(test_client):
    """Test retrieving a non-existent dye by ID."""
    retrieved_dye = dye_service.get_dye_by_id(99999)
    assert retrieved_dye is None

def test_update_dye(test_client):
    """Test updating an existing dye."""
    dye_data = {
        "commercial_name": "Old Dye",
        "code": "OLD-DYE",
        "stock_quantity": 100.0
    }
    dye_dict = dye_service.create_dye(dye_data)

    updated_data = {
        "commercial_name": "New Dye Name",
        "type": "Disperso",
        "concentration": 60.0,
        "stock_quantity": 200.0,
        "validity": datetime(2027, 1, 1)
    }
    updated_dye_dict = dye_service.update_dye(dye_dict['id'], updated_data)

    assert updated_dye_dict is not None
    assert updated_dye_dict['commercial_name'] == updated_data['commercial_name']
    assert updated_dye_dict['type'] == updated_data['type']
    assert updated_dye_dict['concentration'] == updated_data['concentration']
    assert updated_dye_dict['stock_quantity'] == updated_data['stock_quantity']
    assert updated_dye_dict['validity'] == updated_data['validity'].isoformat()

    # Verify changes in DB
    retrieved_dye = Dye.query.get(dye_dict['id'])
    assert retrieved_dye.commercial_name == updated_data['commercial_name']
    assert retrieved_dye.type == updated_data['type']

def test_update_dye_non_existent(test_client):
    """Test updating a non-existent dye."""
    updated_dye = dye_service.update_dye(99999, {"commercial_name": "nonexistent"})
    assert updated_dye is None

def test_delete_dye(test_client):
    """Test deleting an existing dye."""
    dye_data = {
        "commercial_name": "To Delete Dye",
        "code": "DEL-DYE",
    }
    dye_dict = dye_service.create_dye(dye_data)

    result = dye_service.delete_dye(dye_dict['id'])
    assert result is True

    # Verify dye is deleted from DB
    retrieved_dye = Dye.query.get(dye_dict['id'])
    assert retrieved_dye is None

def test_delete_dye_non_existent(test_client):
    """Test deleting a non-existent dye."""
    result = dye_service.delete_dye(99999)
    assert result is False