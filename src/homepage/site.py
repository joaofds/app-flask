from flask import Blueprint, render_template, request

site_bp = Blueprint('site', __name__, template_folder='templates', static_folder='static',
url_prefix='/site')

@site_bp.route('/', methods=['GET'])
def index():
    title = 'Seja bem vindo'
    return render_template('index.html', title=title)

@site_bp.route('/about', methods=['GET'])
def about():
    return render_template('about_us.html')

@site_bp.route('/contact', methods=['GET'])
def contact():
    title = 'Contato'
    return render_template('contact.html', title = title)