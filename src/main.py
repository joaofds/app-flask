from flask import Flask, redirect
from homepage.site import site_bp
from dashboard.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(site_bp)
app.register_blueprint(dashboard_bp)

@app.route('/')
def root():
    return redirect('/site')

if __name__ == "__main__":
    app.run(debug=True)
