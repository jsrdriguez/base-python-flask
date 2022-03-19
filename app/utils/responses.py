from flask import jsonify

def success(message = 'Created'):
  return jsonify({
    'success': True,
    'message': 'Created',
  }), 201

def success_updated(message = 'Updated'):
  return jsonify({
    'success': True,
    'message': message,
  }), 200

def response(data):
  return jsonify({
    'success': True,
    'results': data
  }), 200

def not_found(error = 'not found'):
  return jsonify({
    'success': False,
    'results': None,
    'message': error,
    'code': 404
  }), 404

def bad_request(error = None):
  return jsonify({
    'success': False,
    'results': None,
    'errors': error,
    'message': 'Bad request',
    'code': 400
  }), 400

def server_error(error = None):
  return jsonify({
    'success': False,
    'results': None,
    'errors': error,
    'message': 'Bad request',
    'code': 500
  }), 500