import pytest
from services import raw_material_service
from models.raw_material_model import RawMaterial, db

def test_create_raw_material(test_client):
    """Test creating a new raw material."""
    material_data = {
        "name": "Algodão Fio 30.1",
        "type": "Fio",
        "supplier": "Fiação Teste",
        "technical_characteristics": "100% algodão, penteado",
        "stock_quantity": 1000.5
    }
    material_dict = raw_material_service.create_raw_material(material_data)

    assert material_dict is not None
    assert material_dict['name'] == material_data['name']
    assert material_dict['type'] == material_data['type']
    assert material_dict['stock_quantity'] == material_data['stock_quantity']

    # Verify material exists in the database
    retrieved_material = RawMaterial.query.filter_by(name=material_data['name']).first()
    assert retrieved_material is not None
    assert retrieved_material.type == material_data['type']

def test_create_raw_material_duplicate_name(test_client):
    """Test creating a raw material with a duplicate name."""
    material_data1 = {
        "name": "Algodão Duplicado",
        "type": "Fio",
    }
    material_data2 = {
        "name": "Algodão Duplicado",
        "type": "Tecido",
    }
    raw_material_service.create_raw_material(material_data1)

    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        raw_material_service.create_raw_material(material_data2)

def test_get_all_raw_materials(test_client):
    """Test retrieving all raw materials."""
    raw_material_service.create_raw_material({"name": "Material A", "type": "Fio"})
    raw_material_service.create_raw_material({"name": "Material B", "type": "Tecido"})
    materials = raw_material_service.get_all_raw_materials()
    assert len(materials) >= 2

def test_get_raw_material_by_id(test_client):
    """Test retrieving a raw material by ID."""
    material_data = {
        "name": "Material By ID",
        "type": "Fio",
    }
    created_material_dict = raw_material_service.create_raw_material(material_data)

    retrieved_material_dict = raw_material_service.get_raw_material_by_id(created_material_dict['id'])
    assert retrieved_material_dict is not None
    assert retrieved_material_dict['name'] == material_data['name']
    assert retrieved_material_dict['type'] == material_data['type']

def test_get_raw_material_by_id_non_existent(test_client):
    """Test retrieving a non-existent raw material by ID."""
    retrieved_material = raw_material_service.get_raw_material_by_id(99999)
    assert retrieved_material is None

def test_update_raw_material(test_client):
    """Test updating an existing raw material."""
    material_data = {
        "name": "Old Material",
        "type": "Old Type",
        "stock_quantity": 500.0
    }
    material_dict = raw_material_service.create_raw_material(material_data)

    updated_data = {
        "name": "New Material Name",
        "type": "New Type",
        "supplier": "New Supplier",
        "stock_quantity": 750.0
    }
    updated_material_dict = raw_material_service.update_raw_material(material_dict['id'], updated_data)

    assert updated_material_dict is not None
    assert updated_material_dict['name'] == updated_data['name']
    assert updated_material_dict['type'] == updated_data['type']
    assert updated_material_dict['supplier'] == updated_data['supplier']
    assert updated_material_dict['stock_quantity'] == updated_data['stock_quantity']

    # Verify changes in DB
    retrieved_material = RawMaterial.query.get(material_dict['id'])
    assert retrieved_material.name == updated_data['name']
    assert retrieved_material.type == updated_data['type']

def test_update_raw_material_non_existent(test_client):
    """Test updating a non-existent raw material."""
    updated_material = raw_material_service.update_raw_material(99999, {"name": "nonexistent"})
    assert updated_material is None

def test_delete_raw_material(test_client):
    """Test deleting an existing raw material."""
    material_data = {
        "name": "To Delete Material",
        "type": "Fio",
    }
    material_dict = raw_material_service.create_raw_material(material_data)

    result = raw_material_service.delete_raw_material(material_dict['id'])
    assert result is True

    # Verify material is deleted from DB
    retrieved_material = RawMaterial.query.get(material_dict['id'])
    assert retrieved_material is None

def test_delete_raw_material_non_existent(test_client):
    """Test deleting a non-existent raw material."""
    result = raw_material_service.delete_raw_material(99999)
    assert result is False