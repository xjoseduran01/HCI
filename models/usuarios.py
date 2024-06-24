from utils.db import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    usuarioid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(200))

    def __init__(self, nombre, email, password):

        self.nombre = nombre
        self.email = email
        self.password = password
        
    def serialize(self):
        return {
            'usuarioid': self.UsuarioID,
            'nombre': self.nombre,
            'email': self.email,
            'password': self.password,
        }
