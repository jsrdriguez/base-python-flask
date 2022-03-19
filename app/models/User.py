from . import db

class UserModel(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  names = db.Column(db.String, nullable=False)

  @classmethod
  def new(cls, data):
    return UserModel(
      names=data['names'],
    )

  def save(self):
    try:    
      db.session.add(self)
      db.session.commit()
      db.session.flush()
    except Exception as e:
      return False

  def update(self, _id):
    try:
      sql_update = ('UPDATE persons SET names = :names '  
                    'WHERE id = :id')

      db.session.execute(sql_update, {
        'id': _id,
        'names': self.names
      })
        
      return db.session.commit()
    except:
      return False