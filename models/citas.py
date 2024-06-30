from utils.db import db

class Citas(db.Model):
    __tablename__ = 'citas'
    citasid = db.Column(db.Integer, primary_key=True)
    usuarioid = db.Column(db.Integer)
    areaid = db.Column(db.Integer)
    fecha = db.Column(db.Date)
    horarioid = db.Column(db.Integer)

    def __init__(self, usuarioid, areaid, fecha, horarioid):
        self.usuarioid = usuarioid
        self.areaid = areaid
        self.fecha = fecha
        self.horarioid = horarioid
        
    def serialize(self):
        return {
            'usuarioid': self.usuarioid,
            'areaid': self.areaid,
            'fecha': self.fecha.strftime('%d-%m-%Y') if self.fecha else None,
            'horarioid': self.horarioid
        }
