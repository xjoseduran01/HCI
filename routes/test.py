from flask import Blueprint, jsonify, request
from models.tests import Tests
from utils.db import db
from datetime import datetime

test_bp = Blueprint('test', __name__)

@test_bp.route('/VerTest', methods=['GET'])
def vertest():
    try:
        # Obtener todos los tests
        tests = Tests.query.all()
        
        lista_tests = []
        
       

        # Preparar la respuesta
        data = {
            'message': 'Lista de tests y preguntas con opciones',
            'status': 200,
            'data': lista_tests
        }

        # Devuelve la respuesta JSON
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'message': 'Error al obtener tests y preguntas', 'error': str(e)}), 500


