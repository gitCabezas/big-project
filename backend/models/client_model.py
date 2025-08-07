from . import db

class Client(db.Model):
    """Modelo de dados para um cliente."""
    
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    cnpj_cpf = db.Column(db.String(18), unique=True, nullable=False)
    address = db.Column(db.String(255))
    contact = db.Column(db.String(120))
    observations = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        """Converte o objeto Client para um dicionário."""
        return {
            'id': self.id,
            'name': self.name,
            'cnpj_cpf': self.cnpj_cpf,
            'address': self.address,
            'contact': self.contact,
            'observations': self.observations,
            'is_active': self.is_active
        }

    def __repr__(self):
        return f'<Client {self.name}>'
