 # myapp/views.py
from flask import Blueprint,render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/come')
def home():
    return render_template ('home.html')

