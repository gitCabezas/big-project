from . import db

class RecipeDye(db.Model):
    __tablename__ = 'recipe_dyes'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    dye_id = db.Column(db.Integer, db.ForeignKey('dyes.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    recipe = db.relationship('Recipe', backref=db.backref('recipe_dyes', cascade='all, delete-orphan'))
    dye = db.relationship('Dye')

    def to_dict(self):
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'dye_id': self.dye_id,
            'quantity': self.quantity
        }
