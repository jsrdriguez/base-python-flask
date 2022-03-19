class ParseJsonError(Exception):
  def __init__(self, message, status_code):
    super().__init__(message)
    self.status_code = status_code
    self.message = message
      
  def to_dict(self):
    rv = dict(self.message or ())
    return rv 

  def to_str(self):
    rv = self.message
    return rv 

class UnAuthorizedException(ParseJsonError):
  def __init__(self, message, status_code = 401):
    super().__init__(message, status_code)

class ForbiddenException(ParseJsonError):
  def __init__(self, message, status_code = 403):
    super().__init__(message, status_code)

class BadRequestException(ParseJsonError):
  def __init__(self, message, status_code = 400):
    super().__init__(message, status_code)

  
class NotFountException(ParseJsonError):
  def __init__(self, message, status_code = 404):
    super().__init__(message, status_code)
