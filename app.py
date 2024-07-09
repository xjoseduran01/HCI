from flask import Flask
from routes.login import login_bp
from routes.registro import registro_bp
from routes.datos import data_bp
from routes.nuevacita import citas_bp
from routes.vercita import vercita_bp
from routes.cancelar import cancelar_bp
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from utils.mail import mail_instance, configure_mail
from flask_cors import CORS
from utils.db import db

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'clavesecreta123'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


configure_mail(app)

db.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(data_bp)
app.register_blueprint(citas_bp)
app.register_blueprint(vercita_bp)
app.register_blueprint(cancelar_bp)


if __name__ == '__main__':
  app.run(port=5000)
