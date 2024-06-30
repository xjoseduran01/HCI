from flask import Blueprint, jsonify, request
from models.citas import Citas
from models.areas import Areas
from models.horarios import Horarios
from utils.db import db
from datetime import datetime

citas_bp = Blueprint('cita', __name__)

@citas_bp.route('/programarCita', methods=['POST'])
def nuevaCita():
    try:
        data = request.json
        usuarioid = int(data.get('id'))  # Convertir id a entero
        area_nombre = data.get('selectedArea')
        fecha = data.get('selectedDia')
        horario_desc = data.get('selectedHorario')

        # Buscar el areaid basado en el nombre del área recibido
        area = Areas.query.filter_by(nombre=area_nombre).first()
        if not area:
            return jsonify({'message': 'Área no encontrada', 'status': 404}), 404
        areaid = area.areaid

        # Buscar el horarioid basado en el horario recibido
        horario = Horarios.query.filter_by(horario=horario_desc).first()
        if not horario:
            return jsonify({'message': 'Horario no encontrado', 'status': 404}), 404
        horarioid = horario.horarioid

        # Convertir la fecha al formato correcto para la base de datos
        fecha_formateada = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')

        # Crear una nueva cita
        cita_nueva = Citas(
            usuarioid=usuarioid,
            areaid=areaid,
            fecha=fecha_formateada,
            horarioid=horarioid
        )
        db.session.add(cita_nueva)
        db.session.commit()

        # Preparar la respuesta
        response_data = {
            'message': 'Cita programada correctamente',
            'status': 200,
        }
        return jsonify(response_data), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al procesar las respuestas', 'error': str(e)}), 500
