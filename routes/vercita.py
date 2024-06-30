from flask import Blueprint, jsonify, request
from models.citas import Citas
from models.horarios import Horarios
from models.usuarios import Usuarios
from models.areas import Areas
from utils.db import db
from datetime import datetime
from flask_babel import Babel

vercita_bp = Blueprint('vercita', __name__)



@vercita_bp.route('/VerCita', methods=['GET'])
def ver_cita():
    try:
        citas = Citas.query.all()
        lista_citas = []

        for cita in citas:
            usuario = Usuarios.query.get(cita.usuarioid)
            nombre_usuario = usuario.nombre if usuario else None
            
            area = Areas.query.get(cita.areaid)
            nombre_area = area.nombre if area else None

            horario = Horarios.query.get(cita.horarioid)
            dato_horario = horario.horario if horario else None

            if cita.fecha:
                fechacita = cita.fecha
                dia = fechacita.day
                mes = fechacita.strftime('%b').capitalize()  # Abreviatura del mes en mayúsculas (EJ: JAN, FEB)
                fecha_formateada = fechacita.strftime('%d de %B').capitalize()  # Ejemplo: 5 de Mayo
            else:
                dia = None
                mes = None
                fecha_formateada = None

            cita_data = {
                'nombre_usuario': nombre_usuario,
                'nombre_area': nombre_area,
                'dato_horario': dato_horario,
                'dia': dia,
                'mes': mes,
                'fecha_formateada': fecha_formateada
            }
            lista_citas.append(cita_data)
        
        data = {
            'message': 'Lista de citas',
            'status': 200,
            'data': lista_citas
        }

        return jsonify(data), 200

    except Exception as e:
        return jsonify({'message': 'Error al obtener citas', 'error': str(e)}), 500