import pytz
from datetime import datetime

def date_now():
  return datetime.now(tz=pytz.timezone('America/Lima'))

def current_date():
  x = date_now()
  return f"{x.strftime('%Y-%m-%d')} {x.strftime('%X')}"


    
    