from flask import Flask
from routes import site_bp
from dashboard.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(site_bp)
app.register_blueprint(dashboard_bp)


if __name__ == "__main__":
    app.run(debug=True)
