from . import db
from datetime import datetime

class ChemicalInput(db.Model):
    """Modelo de dados para Insumos Químicos."""
    
    __tablename__ = 'chemical_inputs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    function = db.Column(db.String(100)) # Ex: Auxiliar, Neutralizante, Fixador
    supplier = db.Column(db.String(100))
    concentration = db.Column(db.Float)
    safety_data_sheet_url = db.Column(db.String(255))
    validity = db.Column(db.DateTime)
    stock_quantity = db.Column(db.Float, nullable=False, default=0.0)

    def to_dict(self):
        """Converte o objeto ChemicalInput para um dicionário."""
        return {
            'id': self.id,
            'name': self.name,
            'function': self.function,
            'supplier': self.supplier,
            'concentration': self.concentration,
            'safety_data_sheet_url': self.safety_data_sheet_url,
            'validity': self.validity.isoformat() if self.validity else None,
            'stock_quantity': self.stock_quantity
        }

    def __repr__(self):
        return f'<ChemicalInput {self.name}>'
