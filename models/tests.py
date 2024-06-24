from utils.db import db

class Tests(db.Model):
    __tablename__ = 'tipo_test'
    tipotest_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.Text)


    def __init__(self, tipotest_id, nombre, descripcion):
        self.testid = tipotest_id
        self.titulo = nombre
        self.descripcion = descripcion

        
    def serialize(self):
        return {
            'tipotest_id': self.tipotest_id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
        }