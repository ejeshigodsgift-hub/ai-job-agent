from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")


def send_live_notification(event, data):
    socketio.emit(event, data)