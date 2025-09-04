from models import db
from datetime import datetime

class Recipe(db.Model):
    """Modelo de dados para Receituários."""
    
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    article = db.Column(db.String(100))
    process = db.Column(db.String(100))
    substrate = db.Column(db.String(100))
    machine = db.Column(db.String(100))
    weight_kg = db.Column(db.Float)
    status = db.Column(db.String(50), default='rascunho') # rascunho, aprovado, em uso, descontinuado
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento com o cliente
    client = db.relationship('Client', backref='recipes')

    def to_dict(self):
        """Converte o objeto Recipe para um dicionário."""
        return {
            'id': self.id,
            'name': self.name,
            'client_id': self.client_id,
            'article': self.article,
            'process': self.process,
            'substrate': self.substrate,
            'machine': self.machine,
            'weight_kg': self.weight_kg,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'dyes': [rd.to_dict() for rd in self.recipe_dyes],
            'chemical_inputs': [rci.to_dict() for rci in self.recipe_chemical_inputs]
        }

    def __repr__(self):
        return f'<Recipe {self.name}>'
