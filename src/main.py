from flask import Flask
from routes import site_bp

app = Flask(__name__)

app.register_blueprint(site_bp)