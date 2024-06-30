
from utils.db import db



class Citas(db.Model):
    __tablename__ = 'citas'
    citasid = db.Column(db.Integer, primary_key=True)
    usuarioid = db.Column(db.Integer)
    areaid = db.Column(db.Integer)
    fecha = db.Column(db.Date)
    horarioID = db.Column(db.Integer)

    def __init__(self, citasid, usuarioid, areaid, fecha, horarioid):
        self.citasid = citasid
        self.UsuarioID = usuarioid
        self.areaID = areaid
        self.fecha = fecha
        self.horarioid = horarioid
        
    def serialize(self):
        return {
            'citasid': self.citasid,
            'usuarioid': self.usuarioid,
            'areaid': self.areaid,
            'fecha': self.fecha.strftime('%d-%m-%Y') if self.fecha_test else None,
            'horarioid': self.horarioid
        }
