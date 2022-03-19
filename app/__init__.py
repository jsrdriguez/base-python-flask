from flask import Flask, jsonify
from flasgger import Swagger
from .models import db
from .routes import (
    ApiRoute,
)
from app.utils.exceptions import (
  BadRequestException,
  NotFountException,
  UnAuthorizedException,
  ForbiddenException
)

def create_app(env):    
  app = Flask(__name__)

  app.config.from_object(env)

  if app.config['DEBUG']:
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

  app.register_blueprint(ApiRoute)

  register_handler_exceptions(app)

  db.init_app(app)

  return app

def register_handler_exceptions(app):
  @app.errorhandler(ForbiddenException)
  def forbidden_exception(err):
    return jsonify({
        'success': False,
        'results': None,
        'errors': [],
        'message': err.to_str(),
        'code': 403
    }), 403

  @app.errorhandler(UnAuthorizedException)
  def un_authorized_exception(err):
    return jsonify({
      'success': False,
      'results': None,
      'errors': [],
      'message': err.to_str(),
      'code': 401
    }), 401

  @app.errorhandler(NotFountException)
  def not_found(err):
    return jsonify({
      'success': False,
      'results': None,
      'errors': [],
      'message': err.to_str(),
      'code': 404
    }), 404

  @app.errorhandler(BadRequestException)
  def bad_request(err):
    return jsonify({
      'success': False,
      'results': None,
      'errors': err.to_dict(),
      'message': 'Bad request',
      'code': 400
    }), 400

  @app.errorhandler(Exception)
  def server_error(err):
    return jsonify({
      'success': False,
      'results': None,
      'errors': str(err),
      'message': 'Error server',
      'code': 500
    }), 500