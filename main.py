from flask import Flask
from config import Config
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.jobs_routes import jobs_bp
from routes.billing_routes import billing_bp
from routes.admin_routes import admin_bp

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