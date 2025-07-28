from . import db
from datetime import datetime

class Dye(db.Model):
    """Modelo de dados para Corantes."""
    
    __tablename__ = 'dyes'

    id = db.Column(db.Integer, primary_key=True)
    commercial_name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    manufacturer = db.Column(db.String(100))
    type = db.Column(db.String(50))  # Ex: Reativo, Direto, Disperso
    concentration = db.Column(db.Float)
    validity = db.Column(db.DateTime)
    stock_quantity = db.Column(db.Float, nullable=False, default=0.0)
    lot_number = db.Column(db.String(50))

    def to_dict(self):
        """Converte o objeto Dye para um dicionário."""
        return {
            'id': self.id,
            'commercial_name': self.commercial_name,
            'code': self.code,
            'manufacturer': self.manufacturer,
            'type': self.type,
            'concentration': self.concentration,
            'validity': self.validity.isoformat() if self.validity else None,
            'stock_quantity': self.stock_quantity,
            'lot_number': self.lot_number
        }

    def __repr__(self):
        return f'<Dye {self.commercial_name}>'
