#Database_Model
from repository import db
class User( db.Model ):
    __tablename__ = "user"

    id = db.Column( db.Integer, primary_key = True )
    username = db.Column( db.String( 80 ), nullable = False)
    email = db.Column( db.String( 120 ), unique = True, nullable = False)
    password = db.Column( db.String( 120 ), nullable = False)

#Schema
from flask_marshmallow import Marshmallow
from marshmallow import post_load
class UserSchema( Marshmallow().SQLAlchemyAutoSchema ):
    class Meta:
        model = User
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
