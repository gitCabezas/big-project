from . import db

class Color(db.Model):
    """Modelo de dados para Cores."""
    
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    pantone_rgb = db.Column(db.String(50)) # Código Pantone ou RGB
    client_reference = db.Column(db.String(100))
    # Relacionamento com a receita base será adicionado posteriormente
    # base_recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))

    def to_dict(self):
        """Converte o objeto Color para um dicionário."""
        return {
            'id': self.id,
            'name': self.name,
            'pantone_rgb': self.pantone_rgb,
            'client_reference': self.client_reference
        }

    def __repr__(self):
        return f'<Color {self.name}>'
