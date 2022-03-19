from flask import request, g
from marshmallow import Schema, fields
from marshmallow.validate import Length
from app.utils.exceptions import BadRequestException
from app.utils.responses import (
  bad_request,
)

class UserSchema(Schema):
  class Meta:
    fields = ('id', 'names',)
  
  names = fields.Str(required=True, 
    validate=Length(min=2, error="Names is required"),
    error_messages={
      "required": "Names is required"
    }
  )
    
user_schema = UserSchema()

class UserPostSchema(UserSchema):
  pass

def post_user_validate(function):
  def wrap(*args, **kwargs):
    postData = request.form.to_dict()
        
    if postData is None:
      raise BadRequestException({
          "validation": ["Not found data"]
      })

    errors = UserPostSchema().validate(postData)

    if errors:
      print(errors)
      return bad_request(errors)

    g.data = postData

    return function()

  wrap.__name__ = function.__name__
  return wrap
