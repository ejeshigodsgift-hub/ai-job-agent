from flask_socketio import emit
from services.socket_service import socketio


@socketio.on('connect')
def connect():
    emit('message', {
        'status': 'connected'
    })