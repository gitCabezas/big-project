from models import db
from models.color_model import Color

def get_all_colors():
    """Busca todas as cores."""
    colors = Color.query.all()
    return [color.to_dict() for color in colors]

def get_color_by_id(color_id):
    """Busca uma cor pelo ID."""
    color = Color.query.get(color_id)
    return color.to_dict() if color else None

def create_color(color_data):
    """Cria uma nova cor."""
    new_color = Color(
        name=color_data['name'],
        pantone_rgb=color_data.get('pantone_rgb'),
        client_reference=color_data.get('client_reference')
    )
    db.session.add(new_color)
    db.session.commit()
    return new_color.to_dict()

def update_color(color_id, color_data):
    """Atualiza uma cor."""
    color = Color.query.get(color_id)
    if not color:
        return None

    color.name = color_data.get('name', color.name)
    color.pantone_rgb = color_data.get('pantone_rgb', color.pantone_rgb)
    color.client_reference = color_data.get('client_reference', color.client_reference)

    db.session.commit()
    return color.to_dict()

def delete_color(color_id):
    """Deleta uma cor."""
    color = Color.query.get(color_id)
    if color:
        db.session.delete(color)
        db.session.commit()
        return True
    return False
