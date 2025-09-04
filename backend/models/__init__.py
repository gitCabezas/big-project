from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import User
from .client_model import Client
from .raw_material_model import RawMaterial
from .dye_model import Dye
from .chemical_input_model import ChemicalInput
from .color_model import Color
from .recipe_model import Recipe
from .recipe_dye_model import RecipeDye
from .recipe_chemical_input_model import RecipeChemicalInput