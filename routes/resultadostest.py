# Importación de módulos y clases necesarias
from flask import Blueprint, jsonify, request
from models.test_realizado import testRealizados
from models.usuarios import Usuarios
from models.tests import Tests
from utils.db import db
from datetime import datetime

# Creación de un Blueprint, que es un componente para estructurar la aplicación en módulos
testrealizado_bp = Blueprint('testrealizado', __name__)

# Definición de una ruta en Flask usando el Blueprint creado. 'methods=['GET']' indica que esta ruta solo acepta peticiones GET
@testrealizado_bp.route('/VerTestRealizados', methods=['GET'])
def vertestrealizado():
    try:
        # Consultar todos los objetos de tipo 'testRealizados' desde la base de datos
        tests = testRealizados.query.all()
        
        # Lista para almacenar los tests procesados
        lista_tests = []
        
        # Iterar sobre cada test realizado
        for test in tests:
            # Buscar en la base de datos el usuario asociado al test usando 'usuarioid' y obtener su nombre
            usuario = Usuarios.query.get(test.usuarioid)
            nombre_usuario = usuario.nombre if usuario else None
            
            # Buscar en la base de datos el test específico usando 'tipotest_id' y obtener su nombre
            test_obj = Tests.query.get(test.tipotest_id)
            nombre_test = test_obj.nombre if test_obj else None
            
            # Crear un diccionario con la información del test, formatear la fecha si es necesario
            test_data = {
                'test_id': test.test_id,
                'fecha_test': test.fecha_test.strftime('%Y-%m-%d') if test.fecha_test else None,
                'nombre_usuario': nombre_usuario,
                'nombre_test': nombre_test,
                'puntaje': test.puntaje
            }
            # Agregar el diccionario creado a la lista de tests
            lista_tests.append(test_data)
        
        # Preparar el diccionario que se devolverá como JSON
        data = {
            'message': 'Lista de tests realizados',
            'status': 200,
            'data': lista_tests
        }
 
        # Devolver los datos serializados en formato JSON y el código de estado HTTP 200
        return jsonify(data), 200

    # Manejo de excepciones en caso de errores
    except Exception as e:
        # Devolver un mensaje de error y código de estado HTTP 500
        return jsonify({'message': 'Error al obtener tests realizados', 'error': str(e)}), 500
