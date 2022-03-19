from flask import request, g
from flasgger.utils import swag_from
from app.models.User import UserModel
from app.schemas import (
  post_user_validate
)
from app.utils.responses import (
  success,
  response
)

@swag_from('./../../docs/user/list.yml')
def index():
  try:
    users = [
      {"id" : 1, "name": "Maria"},
      {"id" : 2, "name": "Daniel"},
      {"id" : 3, "name": "Pepito"},
    ]

    return response(users)

  except Exception as err:
    print(err)

@swag_from('./../../docs/user/create.yml')
@post_user_validate
def create():
  try:
    postData = g.data
      
    return success()

  except Exception as err:
    print(err)
    
    


