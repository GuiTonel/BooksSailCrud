from repository import db
from models.user import UserSchema, User

from utils.user import user_schema_dump_return, users_schema_dump_return

user_schema = UserSchema()
users_schema = UserSchema( many = True )

@users_schema_dump_return
def find_users():
    users = User.query.all()
    return users

@user_schema_dump_return
def find_user_by_id( id_usuario ):
    user = User.query.get( id_usuario )
    return user

@user_schema_dump_return
def insert_user( user_json ):
    user = User( user_json['username'], user_json['email'] )

    db.session.add( user )
    db.session.commit()

    return user
