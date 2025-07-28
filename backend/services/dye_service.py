from models import db
from models.dye_model import Dye

def get_all_dyes():
    """Busca todos os corantes."""
    dyes = Dye.query.all()
    return [dye.to_dict() for dye in dyes]

def get_dye_by_id(dye_id):
    """Busca um corante pelo ID."""
    dye = Dye.query.get(dye_id)
    return dye.to_dict() if dye else None

def create_dye(dye_data):
    """Cria um novo corante."""
    new_dye = Dye(
        commercial_name=dye_data['commercial_name'],
        code=dye_data['code'],
        manufacturer=dye_data.get('manufacturer'),
        type=dye_data.get('type'),
        concentration=dye_data.get('concentration'),
        validity=dye_data.get('validity'),
        stock_quantity=dye_data.get('stock_quantity', 0.0),
        lot_number=dye_data.get('lot_number')
    )
    db.session.add(new_dye)
    db.session.commit()
    return new_dye.to_dict()

def update_dye(dye_id, dye_data):
    """Atualiza um corante."""
    dye = Dye.query.get(dye_id)
    if not dye:
        return None

    dye.commercial_name = dye_data.get('commercial_name', dye.commercial_name)
    dye.code = dye_data.get('code', dye.code)
    dye.manufacturer = dye_data.get('manufacturer', dye.manufacturer)
    dye.type = dye_data.get('type', dye.type)
    dye.concentration = dye_data.get('concentration', dye.concentration)
    dye.validity = dye_data.get('validity', dye.validity)
    dye.stock_quantity = dye_data.get('stock_quantity', dye.stock_quantity)
    dye.lot_number = dye_data.get('lot_number', dye.lot_number)

    db.session.commit()
    return dye.to_dict()

def delete_dye(dye_id):
    """Deleta um corante."""
    dye = Dye.query.get(dye_id)
    if dye:
        db.session.delete(dye)
        db.session.commit()
        return True
    return False
