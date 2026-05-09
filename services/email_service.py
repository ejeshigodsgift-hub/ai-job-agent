from flask_mail import Mail
from flask_mail import Message
from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'

mail = Mail(app)


def send_email(receiver, message):
    msg = Message(
        subject='AI Job Agent',
        sender='your_email@gmail.com',
        recipients=[receiver]
    )

    msg.body = message

    mail.send(msg)