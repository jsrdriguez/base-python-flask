class LocalConfig:
  DEBUG                          =  True
  SQLALCHEMY_DATABASE_URI        =  'postgresql://user:password@server:port/bd'
  SQLALCHEMY_TRACK_MODIFICATIONS =  False
  PROPAGATE_EXCEPTIONS           =  True
  SECRET_KEY                     =  'development'
  STATIC_FOLDER                  =  './static/'
  UPLOAD_FOLDER                  =  './static/profiles/'
  UPLOAD_REPORT                  =  './static/reports/'
  UPLOAD_EXTENSIONS              =  ['.jpg', '.png', '.jpeg']
  #EMAIL
  SWAGGER = {
    "title": 'API - Documentación',
    "footer_text": '',
    "specs_route": '/apidocs/',
    "uiversion": 3
  }
  SWAGGER_TEMPLATE = {
    "swagger": '2.0',
    "info": {
      "title": 'API - Documentación',
      "version": '0.1.1',
      "contact": {
        "name": 'Api',
      }
    },
    "securityDefinitions": {},
    "security": [
      {
        "Bearer": [ ]
      }
    ]
  }