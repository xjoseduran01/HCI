from flask import Blueprint, jsonify, request
from models.usuarios import Usuarios

from utils.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash

# Crea un Blueprint para la autenticación
registro_bp = Blueprint('registrar_usuarios', __name__)

@registro_bp.route('/registrar', methods=['POST'])
def registro():
    try:
        datos_usuario = request.get_json()

        if Usuarios.query.filter_by(email=datos_usuario['email']).first():
            return jsonify({'message': 'El correo electrónico ya está en uso'}), 400

        nuevo_estudiante = Usuarios(
            nombre=datos_usuario['nombre'],
            email=datos_usuario['email'],
            password=datos_usuario['password']
        )

        db.session.add(nuevo_estudiante)
        db.session.commit()

        resultado = {
            'usuarioid': nuevo_estudiante.usuarioid,
            'nombre': nuevo_estudiante.nombre,
            'email': nuevo_estudiante.email
        }
        data = {
            'message': 'Nuevo usuario registrado exitosamente',
            'status': 201,
            'data': resultado
        }
        return jsonify(data), 201

    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return jsonify({'message': 'Error al registrar', 'error': str(e)}), 500

