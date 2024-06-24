from flask import Blueprint, jsonify, request
from models.test_realizado import testRealizados
from models.usuarios import Usuarios
from models.tests import Tests
from utils.db import db
from datetime import datetime

test_fecha_id_bp = Blueprint('testfecha_id', __name__)

@test_fecha_id_bp.route('/VerTestFecha', methods=['GET'])
def vertestfecha():
    try:
        # Obtener parámetros de filtro desde la solicitud
        fecha_test = request.args.get('fecha_test')
        tipo_test = request.args.get('tipo_test')
        puntaje_obtenido = request.args.get('puntaje_obtenido')
        
        # Construir la consulta de base de datos
        query = testRealizados.query
        
        if fecha_test:
            fecha_test_dt = datetime.strptime(fecha_test, '%Y-%m-%d')
            query = query.filter(testRealizados.fecha_test == fecha_test_dt)
        
        if tipo_test:
            query = query.filter(testRealizados.tipotest_id == int(tipo_test))
        
        if puntaje_obtenido:
            query = query.filter(testRealizados.puntaje >= int(puntaje_obtenido))
        
        # Ejecutar la consulta
        tests = query.all()
        
        lista_tests = []
        
        for test in tests:
            # Obtener el nombre del usuario asociado al usuarioid
            usuario = Usuarios.query.get(test.usuarioid)
            nombre_usuario = usuario.nombre if usuario else None
            
            # Obtener el nombre del test asociado al tipotest_id
            test_obj = Tests.query.get(test.tipotest_id)
            nombre_test = test_obj.nombre if test_obj else None
            
            # Crear un diccionario para cada test realizado y serializarlo
            test_data = {
                'test_id': test.test_id,
                'fecha_test': test.fecha_test.strftime('%Y-%m-%d') if test.fecha_test else None,
                'nombre_usuario': nombre_usuario,
                'nombre_test': nombre_test,
                'puntaje': test.puntaje
            }
            lista_tests.append(test_data)
        
        # Preparar la respuesta
        data = {
            'message': 'Lista de tests realizados',
            'status': 200,
            'data': lista_tests
        }

        # Devolver la respuesta JSON
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'message': 'Error al obtener tests realizados', 'error': str(e)}), 500