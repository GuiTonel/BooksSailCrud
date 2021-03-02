#Database_Model
from repository import db
class User( db.Model ):
    def __init__(self, username, email ):
        super().__init__()
        self.username = username
        self.email = email

    __tablename__ = "user"

    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String( 80 ), nullable = False)
    email = db.Column( db.String( 120 ), unique = True, nullable = False)

#Schema
from flask_marshmallow import Marshmallow
class UserSchema( Marshmallow().SQLAlchemyAutoSchema ):
    class Meta:
        model = User
