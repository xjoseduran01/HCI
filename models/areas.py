from utils.db import db

class Areas(db.Model):
    __tablename__ = 'area'
    areaid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

    def __init__(self, areaid, nombre):
        self.areaid = areaid
        self.nombre = nombre
        
    def serialize(self):
        return {
            'areaid': self.areaid,
            'nombre': self.nombre
        }
