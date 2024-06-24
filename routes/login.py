from flask import Blueprint, jsonify, request
from models.usuarios import Usuarios
from utils.db import db
from datetime import datetime
from werkzeug.security import check_password_hash

# Crear un Blueprint para las rutas de autenticación
login_bp = Blueprint('usuarios', __name__)
    
@login_bp.route('/ListaUsuarios', methods=['GET'])
def obtener_usuarios():
    try:
        usuarios = Usuarios.query.all()
        lista_usuarios = []
        for usuario in usuarios:
            usuario_data = {
                'email': usuario.email,
                'password': usuario.password
            }
            lista_usuarios.append(usuario_data)

        # Preparar la respuesta
        data = {
            'message': 'Lista de usuarios',
            'status': 200,
            'data': lista_usuarios
        }

        # Devuelve la respuesta JSON
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'message': 'Error al obtener usuarios', 'error': str(e)}), 500




@login_bp.route('/Login2', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Email y password son requeridos'}), 400

        email = data.get('email')
        password = data.get('password')

        usuario = Usuarios.query.filter_by(email=email).first()
        if usuario:
           
            if usuario.password == password:
                response = {
                    'message': 'Inicio de sesión exitoso',
                    'status': 200,
                    'data': {
                        'usuarioId': usuario.usuarioid,
                        'nombre': usuario.nombre,
                        'email': usuario.email,
                    }
                }
                return jsonify(response), 200
            else:
                return jsonify({'message': 'Contraseña incorrecta', 'email': email}), 401
        else:
            return jsonify({'message': 'Usuario no encontrado', 'email': email}), 401

    except Exception as e:
        return jsonify({'message': 'Error al iniciar sesión', 'error': str(e)}), 500