import pytest
from services import recipe_service, client_service
from models.recipe_model import Recipe, db
from models.client_model import Client

# Helper function to create a client for testing recipes
def create_test_client():
    client_data = {
        "name": "Test Client for Recipe",
        "cnpj_cpf": "99.999.999/0001-99",
        "address": "Recipe Client Address",
        "contact": "recipe@example.com",
        "observations": "For recipe tests"
    }
    return client_service.create_client(client_data)

def test_create_recipe(test_client):
    """Test creating a new recipe."""
    client_dict = create_test_client()
    recipe_data = {
        "name": "Receita Teste 001",
        "client_id": client_dict['id'],
        "article": "Artigo X",
        "process": "Tingimento",
        "substrate": "Algodão",
        "machine": "Máquina A",
        "weight_kg": 100.0,
        "status": "aprovado"
    }
    recipe_dict = recipe_service.create_recipe(recipe_data)

    assert recipe_dict is not None
    assert recipe_dict['name'] == recipe_data['name']
    assert recipe_dict['client_id'] == recipe_data['client_id']
    assert recipe_dict['status'] == recipe_data['status']
    assert 'created_at' in recipe_dict
    assert 'updated_at' in recipe_dict

    # Verify recipe exists in the database
    retrieved_recipe = Recipe.query.filter_by(name=recipe_data['name']).first()
    assert retrieved_recipe is not None
    assert retrieved_recipe.client_id == recipe_data['client_id']

def test_create_recipe_missing_client_id(test_client):
    """Test creating a recipe without a client_id (should fail)."""
    recipe_data = {
        "name": "Receita Sem Cliente",
        # "client_id": missing
        "article": "Artigo Y",
    }
    with pytest.raises(Exception): # Expecting an IntegrityError or similar
        recipe_service.create_recipe(recipe_data)

def test_get_all_recipes(test_client):
    """Test retrieving all recipes."""
    client_dict = create_test_client()
    recipe_service.create_recipe({"name": "Receita A", "client_id": client_dict['id']})
    recipe_service.create_recipe({"name": "Receita B", "client_id": client_dict['id']})
    recipes = recipe_service.get_all_recipes()
    assert len(recipes) >= 2

def test_get_recipe_by_id(test_client):
    """Test retrieving a recipe by ID."""
    client_dict = create_test_client()
    recipe_data = {
        "name": "Receita By ID",
        "client_id": client_dict['id'],
    }
    created_recipe_dict = recipe_service.create_recipe(recipe_data)

    retrieved_recipe_dict = recipe_service.get_recipe_by_id(created_recipe_dict['id'])
    assert retrieved_recipe_dict is not None
    assert retrieved_recipe_dict['name'] == recipe_data['name']
    assert retrieved_recipe_dict['client_id'] == recipe_data['client_id']

def test_get_recipe_by_id_non_existent(test_client):
    """Test retrieving a non-existent recipe by ID."""
    retrieved_recipe = recipe_service.get_recipe_by_id(99999)
    assert retrieved_recipe is None

def test_update_recipe(test_client):
    """Test updating an existing recipe."""
    client_dict = create_test_client()
    recipe_data = {
        "name": "Old Recipe Name",
        "client_id": client_dict['id'],
        "status": "rascunho"
    }
    recipe_dict = recipe_service.create_recipe(recipe_data)

    updated_data = {
        "name": "New Recipe Name",
        "status": "aprovado",
        "weight_kg": 150.0
    }
    updated_recipe_dict = recipe_service.update_recipe(recipe_dict['id'], updated_data)

    assert updated_recipe_dict is not None
    assert updated_recipe_dict['name'] == updated_data['name']
    assert updated_recipe_dict['status'] == updated_data['status']
    assert updated_recipe_dict['weight_kg'] == updated_data['weight_kg']

    # Verify changes in DB
    retrieved_recipe = Recipe.query.get(recipe_dict['id'])
    assert retrieved_recipe.name == updated_data['name']
    assert retrieved_recipe.status == updated_data['status']

def test_update_recipe_non_existent(test_client):
    """Test updating a non-existent recipe."""
    updated_recipe = recipe_service.update_recipe(99999, {"name": "nonexistent"})
    assert updated_recipe is None

def test_delete_recipe(test_client):
    """Test deleting an existing recipe."""
    client_dict = create_test_client()
    recipe_data = {
        "name": "To Delete Recipe",
        "client_id": client_dict['id'],
    }
    recipe_dict = recipe_service.create_recipe(recipe_data)

    result = recipe_service.delete_recipe(recipe_dict['id'])
    assert result is True

    # Verify recipe is deleted from DB
    retrieved_recipe = Recipe.query.get(recipe_dict['id'])
    assert retrieved_recipe is None

def test_delete_recipe_non_existent(test_client):
    """Test deleting a non-existent recipe."""
    result = recipe_service.delete_recipe(99999)
    assert result is False