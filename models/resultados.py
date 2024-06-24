from utils.db import db

class Resultados(db.Model):
    __tablename__ = 'resultados'
    resultadoid = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer)
    resultado = db.Column(db.Text)
    fecha_completado = db.Column(db.DateTime)

    def __init__(self, resultadoid, test_id, resultado, fecha_completado):
        self.resultadoid = resultadoid
        self.test_id = test_id
        self.resultado = resultado
        self.fecha_completado = fecha_completado
        
    def serialize(self):
        return {
            'resultadoid': self.resultadoid,
            'test_id': self.test_id,
            'resultado': self.resultado,
            'fecha_completado': self.fecha_completado.isoformat() if self.fecha_completado else None,
        }