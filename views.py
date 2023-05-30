from flask import Blueprint

k2test_bp = Blueprint('k2test', __name__)

@k2test_bp.route('/new')
def new_component():
    return 'нова встановлена компонента'
