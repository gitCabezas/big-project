from . import db

class RawMaterial(db.Model):
    """Modelo de dados para Matéria-Prima."""
    
    __tablename__ = 'raw_materials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    type = db.Column(db.String(50), nullable=False)  # Ex: Algodão, Poliéster
    supplier = db.Column(db.String(100))
    technical_characteristics = db.Column(db.Text)
    stock_quantity = db.Column(db.Float, nullable=False, default=0.0)

    def to_dict(self):
        """Converte o objeto RawMaterial para um dicionário."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'supplier': self.supplier,
            'technical_characteristics': self.technical_characteristics,
            'stock_quantity': self.stock_quantity
        }

    def __repr__(self):
        return f'<RawMaterial {self.name}>'
