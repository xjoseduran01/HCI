from utils.db import db

from utils.db import db

class Horarios(db.Model):
    __tablename__ = 'horario'
    horarioid = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.String(20))

    def __init__(self, horarioid,horario):
        self.horarioid = horarioid
        self.horario = horario
        
    def serialize(self):
        return {
            'horarioid': self.horarioid,
            'horario': self.horario
        }
