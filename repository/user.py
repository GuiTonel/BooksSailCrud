from repository import db
from models.user import UserSchema, User

user_schema = UserSchema()
users_schema = UserSchema( many = True )

def find_users():
    users = User.query.all()
    print( user_schema.dumps( users ) )
    return user_schema.dumps( users )

def find_user_by_id( id_usuario ):
    user = User.query.get( id_usuario )
    return user_schema.dump( user )

def insert_user( user_json ):
    user = User( user_json['username'], user_json['email'] )

    db.session.add( user )
    db.session.commit()

    return user_schema.dump( user )
