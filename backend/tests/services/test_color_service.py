import pytest
from services import color_service
from models.color_model import Color, db

def test_create_color(test_client):
    """Test creating a new color."""
    color_data = {
        "name": "Vermelho Vivo",
        "pantone_rgb": "PANTONE 18-1664 TCX",
        "client_reference": "REF-CLI-001"
    }
    color_dict = color_service.create_color(color_data)

    assert color_dict is not None
    assert color_dict['name'] == color_data['name']
    assert color_dict['pantone_rgb'] == color_data['pantone_rgb']

    # Verify color exists in the database
    retrieved_color = Color.query.filter_by(name=color_data['name']).first()
    assert retrieved_color is not None
    assert retrieved_color.pantone_rgb == color_data['pantone_rgb']

def test_create_color_duplicate_name(test_client):
    """Test creating a color with a duplicate name."""
    color_data1 = {
        "name": "Cor Duplicada",
        "pantone_rgb": "RGB(0,0,0)",
    }
    color_data2 = {
        "name": "Cor Duplicada",
        "pantone_rgb": "RGB(255,255,255)",
    }
    color_service.create_color(color_data1)

    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        color_service.create_color(color_data2)

def test_get_all_colors(test_client):
    """Test retrieving all colors."""
    color_service.create_color({"name": "Cor A", "pantone_rgb": "A"})
    color_service.create_color({"name": "Cor B", "pantone_rgb": "B"})
    colors = color_service.get_all_colors()
    assert len(colors) >= 2

def test_get_color_by_id(test_client):
    """Test retrieving a color by ID."""
    color_data = {
        "name": "Cor By ID",
        "pantone_rgb": "ID",
    }
    created_color_dict = color_service.create_color(color_data)

    retrieved_color_dict = color_service.get_color_by_id(created_color_dict['id'])
    assert retrieved_color_dict is not None
    assert retrieved_color_dict['name'] == color_data['name']
    assert retrieved_color_dict['pantone_rgb'] == color_data['pantone_rgb']

def test_get_color_by_id_non_existent(test_client):
    """Test retrieving a non-existent color by ID."""
    retrieved_color = color_service.get_color_by_id(99999)
    assert retrieved_color is None

def test_update_color(test_client):
    """Test updating an existing color."""
    color_data = {
        "name": "Old Color",
        "pantone_rgb": "OLD",
        "client_reference": "OLD-REF"
    }
    color_dict = color_service.create_color(color_data)

    updated_data = {
        "name": "New Color Name",
        "pantone_rgb": "NEW",
        "client_reference": "NEW-REF"
    }
    updated_color_dict = color_service.update_color(color_dict['id'], updated_data)

    assert updated_color_dict is not None
    assert updated_color_dict['name'] == updated_data['name']
    assert updated_color_dict['pantone_rgb'] == updated_data['pantone_rgb']
    assert updated_color_dict['client_reference'] == updated_data['client_reference']

    # Verify changes in DB
    retrieved_color = Color.query.get(color_dict['id'])
    assert retrieved_color.name == updated_data['name']
    assert retrieved_color.pantone_rgb == updated_data['pantone_rgb']

def test_update_color_non_existent(test_client):
    """Test updating a non-existent color."""
    updated_color = color_service.update_color(99999, {"name": "nonexistent"})
    assert updated_color is None

def test_delete_color(test_client):
    """Test deleting an existing color."""
    color_data = {
        "name": "To Delete Color",
        "pantone_rgb": "DEL",
    }
    color_dict = color_service.create_color(color_data)

    result = color_service.delete_color(color_dict['id'])
    assert result is True

    # Verify color is deleted from DB
    retrieved_color = Color.query.get(color_dict['id'])
    assert retrieved_color is None

def test_delete_color_non_existent(test_client):
    """Test deleting a non-existent color."""
    result = color_service.delete_color(99999)
    assert result is False