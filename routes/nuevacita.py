from flask import Blueprint, jsonify, request
from models.citas import Citas
from models.areas import Areas
from models.horarios import Horarios
from utils.db import db
from datetime import datetime
from flask_mail import Message
from utils.mail import mail_instance
from flask import flash, session, jsonify

citas_bp = Blueprint('cita', __name__)

@citas_bp.route('/programarCita', methods=['POST'])
def nuevaCita():
    try:
        data = request.json
        usuarioid = int(data.get('id'))  # Convertir id a entero
        area_nombre = data.get('selectedArea')
        nombredoctor = data.get('selectedDoctor')
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
            horarioid=horarioid,
            doctor = nombredoctor
        )
        db.session.add(cita_nueva)
        db.session.commit()



        enviar_correo(nombredoctor,area_nombre, horario_desc)

        # Preparar la respuesta
        response_data = {
            'message': 'Cita programada correctamente',
            'status': 200,
        }
        return jsonify(response_data), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error al procesar las respuestas', 'error': str(e)}), 500
    

def enviar_correo(nombredoctor,area_nombre, horario_desc):
    correo_usuario = 'jhosselin.clemente@unmsm.edu.pe'
    if not correo_usuario:
        return jsonify({"error": "correo_usuario is not set in session"}), 400

    msg = Message(
        'Datos de diagnóstico',
        sender='sisvita.fisi@gmail.com',  
        recipients=[correo_usuario]       
    )
    msg.body = f'''
    <html>
    <body>
        <h2>Su cita medica se ha registrado correctamente</h2>
        <p><strong>Doctor a cargo:</strong> {nombredoctor}</p>
        <p><strong>Área:</strong> {area_nombre}</p>
        <p><strong>Horario:</strong> {horario_desc}</p>
    </body>
    </html>
    '''

    msg.html = msg.body

    try:
        mail_instance.send(msg)
        flash("Correo enviado correctamente")
        return jsonify({"message": "Correo enviado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
