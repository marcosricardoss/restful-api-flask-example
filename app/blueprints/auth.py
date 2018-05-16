from flask import Blueprint

from app.controllers.authcontroller import AuthController

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    return AuthController().register()

    