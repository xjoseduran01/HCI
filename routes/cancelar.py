from flask import Blueprint, jsonify, request
from models.citas import Citas
from utils.db import db

cancelar_bp = Blueprint('cancelar', __name__)

@cancelar_bp.route('/cancelarCita', methods=['POST'])
def cancelarCita():
    try:
        data = request.json
        citasid = data.get('citasid')

        # Buscar la cita por ID
        cita = Citas.query.get(citasid)
        
        if not cita:
            return jsonify({'message': 'Cita no encontrada', 'status': 404}), 404

        # Eliminar la cita
        db.session.delete(cita)
        db.session.commit()

        # Preparar la respuesta
        response_data = {
            'message': 'Cita eliminada correctamente',
            'status': 200,
        }
        return jsonify(response_data), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al procesar la solicitud', 'error': str(e)}), 500

