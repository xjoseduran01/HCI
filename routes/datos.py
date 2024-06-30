from flask import Blueprint, jsonify
from models.areas import Areas
from models.horarios import Horarios

data_bp = Blueprint('data', __name__)

@data_bp.route('/enviarDatos', methods=['GET'])
def datos():
    try:
        # Obtener todas las áreas
        areas = Areas.query.all()
        lista_areas = [area.serialize() for area in areas]
        
        # Obtener todos los horarios
        horarios = Horarios.query.all()
        lista_horarios = [horario.serialize() for horario in horarios]
        
        data = {
            'message': 'Lista de áreas y horarios',
            'status': 200,
            'areas': lista_areas,
            'horarios': lista_horarios
        }
        
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'message': 'Error al obtener áreas y horarios', 'error': str(e)}), 500
