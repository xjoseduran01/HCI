from flask_mail import Mail, Message

class MailConfig:
    SECRET_KEY = '123456'
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'Sisvita.fisi@gmail.com'
    MAIL_PASSWORD = 'lxctvvfjeyizdmys'

mail_instance = Mail()

def configure_mail(app):
    app.config.from_object(MailConfig)
    mail_instance.init_app(app)
