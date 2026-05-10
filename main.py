from flask import Flask
from config import Config
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.jobs_routes import jobs_bp
from routes.billing_routes import billing_bp
from routes.admin_routes import admin_bp
from routes.chat_routes import chat_bp
from services.socket_service import socketio
from services.cors_service import enable_cors
from services.rate_limit_service import limiter


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(billing_bp)
app.register_blueprint(admin_bp)

@app.route("/")
def home():
    return {
        "status": "running",
        "system": "AI Job Agent"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

app.register_blueprint(chat_bp)


socketio.init_app(app)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)

enable_cors(app)

limiter.init_app(app)