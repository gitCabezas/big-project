from models import db
from models.chemical_input_model import ChemicalInput

def get_all_chemical_inputs():
    """Busca todos os insumos químicos."""
    inputs = ChemicalInput.query.all()
    return [input.to_dict() for input in inputs]

def get_chemical_input_by_id(input_id):
    """Busca um insumo químico pelo ID."""
    input = ChemicalInput.query.get(input_id)
    return input.to_dict() if input else None

def create_chemical_input(input_data):
    """Cria um novo insumo químico."""
    new_input = ChemicalInput(
        name=input_data['name'],
        function=input_data.get('function'),
        supplier=input_data.get('supplier'),
        concentration=input_data.get('concentration'),
        safety_data_sheet_url=input_data.get('safety_data_sheet_url'),
        validity=input_data.get('validity'),
        stock_quantity=input_data.get('stock_quantity', 0.0)
    )
    db.session.add(new_input)
    db.session.commit()
    return new_input.to_dict()

def update_chemical_input(input_id, input_data):
    """Atualiza um insumo químico."""
    input = ChemicalInput.query.get(input_id)
    if not input:
        return None

    input.name = input_data.get('name', input.name)
    input.function = input_data.get('function', input.function)
    input.supplier = input_data.get('supplier', input.supplier)
    input.concentration = input_data.get('concentration', input.concentration)
    input.safety_data_sheet_url = input_data.get('safety_data_sheet_url', input.safety_data_sheet_url)
    input.validity = input_data.get('validity', input.validity)
    input.stock_quantity = input_data.get('stock_quantity', input.stock_quantity)

    db.session.commit()
    return input.to_dict()

def delete_chemical_input(input_id):
    """Deleta um insumo químico."""
    input = ChemicalInput.query.get(input_id)
    if input:
        db.session.delete(input)
        db.session.commit()
        return True
    return False
