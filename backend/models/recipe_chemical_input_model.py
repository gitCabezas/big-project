from . import db

class RecipeChemicalInput(db.Model):
    __tablename__ = 'recipe_chemical_inputs'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    chemical_input_id = db.Column(db.Integer, db.ForeignKey('chemical_inputs.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    recipe = db.relationship('Recipe', backref=db.backref('recipe_chemical_inputs', cascade='all, delete-orphan'))
    chemical_input = db.relationship('ChemicalInput')

    def to_dict(self):
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'chemical_input_id': self.chemical_input_id,
            'quantity': self.quantity
        }
