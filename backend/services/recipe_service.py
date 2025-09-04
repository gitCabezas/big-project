from models import db
from models.recipe_model import Recipe
from models.recipe_dye_model import RecipeDye
from models.recipe_chemical_input_model import RecipeChemicalInput

def get_all_recipes():
    """Busca todos os receituários."""
    recipes = Recipe.query.all()
    return [recipe.to_dict() for recipe in recipes]

def get_recipe_by_id(recipe_id):
    """Busca um receituário pelo ID."""
    recipe = Recipe.query.get(recipe_id)
    return recipe.to_dict() if recipe else None

def create_recipe(recipe_data):
    """Cria um novo receituário."""
    new_recipe = Recipe(
        name=recipe_data['name'],
        client_id=recipe_data['client_id'],
        article=recipe_data.get('article'),
        process=recipe_data.get('process'),
        substrate=recipe_data.get('substrate'),
        machine=recipe_data.get('machine'),
        weight_kg=recipe_data.get('weight_kg'),
        status=recipe_data.get('status', 'rascunho')
    )
    db.session.add(new_recipe)
    db.session.flush()  # Flush to get the new_recipe.id

    if 'dyes' in recipe_data:
        for dye_data in recipe_data['dyes']:
            new_recipe_dye = RecipeDye(
                recipe_id=new_recipe.id,
                dye_id=dye_data['dye_id'],
                quantity=dye_data['quantity']
            )
            db.session.add(new_recipe_dye)

    if 'chemical_inputs' in recipe_data:
        for chemical_input_data in recipe_data['chemical_inputs']:
            new_recipe_chemical_input = RecipeChemicalInput(
                recipe_id=new_recipe.id,
                chemical_input_id=chemical_input_data['chemical_input_id'],
                quantity=chemical_input_data['quantity']
            )
            db.session.add(new_recipe_chemical_input)

    db.session.commit()
    return new_recipe.to_dict()

def update_recipe(recipe_id, recipe_data):
    """Atualiza um receituário existente."""
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return None

    recipe.name = recipe_data.get('name', recipe.name)
    recipe.client_id = recipe_data.get('client_id', recipe.client_id)
    recipe.article = recipe_data.get('article', recipe.article)
    recipe.process = recipe_data.get('process', recipe.process)
    recipe.substrate = recipe_data.get('substrate', recipe.substrate)
    recipe.machine = recipe_data.get('machine', recipe.machine)
    recipe.weight_kg = recipe_data.get('weight_kg', recipe.weight_kg)
    recipe.status = recipe_data.get('status', recipe.status)
    
    db.session.commit()
    return recipe.to_dict()

def delete_recipe(recipe_id):
    """Deleta um receituário."""
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return True
    return False
