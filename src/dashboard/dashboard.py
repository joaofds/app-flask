from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__, template_folder = 'templates',
url_prefix='/dashboard', static_folder='static')

@dashboard_bp.route('/')
@dashboard_bp.route('/home')
def dash_home():
    return render_template('home.html')