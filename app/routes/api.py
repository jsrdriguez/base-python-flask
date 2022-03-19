from flask import Blueprint
from app.middlewares import verify
from app.controllers import (
  UserController
)

api = Blueprint('api_bp', __name__,  url_prefix='/api/v1/')

api.before_request(verify)

api.route('/users', methods=['GET'])(UserController.index)

