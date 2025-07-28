from models import db
from models.raw_material_model import RawMaterial

def get_all_raw_materials():
    """Busca todas as matérias-primas."""
    materials = RawMaterial.query.all()
    return [material.to_dict() for material in materials]

def get_raw_material_by_id(material_id):
    """Busca uma matéria-prima pelo ID."""
    material = RawMaterial.query.get(material_id)
    return material.to_dict() if material else None

def create_raw_material(material_data):
    """Cria uma nova matéria-prima."""
    new_material = RawMaterial(
        name=material_data['name'],
        type=material_data['type'],
        supplier=material_data.get('supplier'),
        technical_characteristics=material_data.get('technical_characteristics'),
        stock_quantity=material_data.get('stock_quantity', 0.0)
    )
    db.session.add(new_material)
    db.session.commit()
    return new_material.to_dict()

def update_raw_material(material_id, material_data):
    """Atualiza uma matéria-prima."""
    material = RawMaterial.query.get(material_id)
    if not material:
        return None

    material.name = material_data.get('name', material.name)
    material.type = material_data.get('type', material.type)
    material.supplier = material_data.get('supplier', material.supplier)
    material.technical_characteristics = material_data.get('technical_characteristics', material.technical_characteristics)
    material.stock_quantity = material_data.get('stock_quantity', material.stock_quantity)

    db.session.commit()
    return material.to_dict()

def delete_raw_material(material_id):
    """Deleta uma matéria-prima."""
    material = RawMaterial.query.get(material_id)
    if material:
        db.session.delete(material)
        db.session.commit()
        return True
    return False
