from flask import Blueprint, jsonify, request
from models.citas import Citas
from models.horarios import Horarios
from models.usuarios import Usuarios
from models.areas import Areas
from utils.db import db
from datetime import datetime

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

            nombredoctor=cita.doctor

            horario = Horarios.query.get(cita.horarioid)
            dato_horario = horario.horario if horario else None

            if cita.fecha:
                fechacita = cita.fecha
                dia = fechacita.day
                mes = fechacita.strftime('%b').upper()  # Abreviatura del mes en mayúsculas (EJ: JAN, FEB)
                fecha_formateada = fechacita.strftime('%d de %B')  # Ejemplo: 5 de Mayo
            else:
                dia = None
                mes = None
                fecha_formateada = None

            cita_data = {
                'citasid': cita.citasid,
                'nombreUsuario': nombre_usuario,
                'nombreArea': nombre_area,
                'nombreDoctor': nombredoctor,
                'datoHorario': dato_horario,
                'dia': dia,
                'mes': mes,
                'fechaFormateada': fecha_formateada
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