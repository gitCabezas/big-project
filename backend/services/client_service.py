from models import db
from models.client_model import Client

def get_all_clients():
    """Busca todos os clientes ativos no banco de dados."""
    clients = Client.query.filter_by(is_active=True).all()
    return [client.to_dict() for client in clients]

def get_client_by_id(client_id):
    """Busca um cliente pelo seu ID."""
    client = Client.query.get(client_id)
    return client.to_dict() if client else None

def create_client(client_data):
    """Cria um novo cliente."""
    new_client = Client(
        name=client_data['name'],
        cnpj_cpf=client_data['cnpj_cpf'],
        address=client_data.get('address'),
        contact=client_data.get('contact'),
        observations=client_data.get('observations')
    )
    db.session.add(new_client)
    db.session.commit()
    return new_client.to_dict()

def update_client(client_id, client_data):
    """Atualiza um cliente existente."""
    client = Client.query.get(client_id)
    if not client:
        return None

    client.name = client_data.get('name', client.name)
    client.cnpj_cpf = client_data.get('cnpj_cpf', client.cnpj_cpf)
    client.address = client_data.get('address', client.address)
    client.contact = client_data.get('contact', client.contact)
    client.observations = client_data.get('observations', client.observations)
    
    db.session.commit()
    return client.to_dict()

def deactivate_client(client_id):
    """Desativa um cliente (soft delete)."""
    client = Client.query.get(client_id)
    if not client:
        return None

    client.is_active = False
    db.session.commit()
    return client.to_dict()

def delete_client(client_id):
    """Deleta um cliente (hard delete)."""
    client = Client.query.get(client_id)
    if not client:
        return None

    db.session.delete(client)
    db.session.commit()
    return True
