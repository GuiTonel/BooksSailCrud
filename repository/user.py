from repository import db
from models.user import User

from utils.user import *

@user_schema_dump_return
def find_users():
    users = User.query.all()
    return users

@user_schema_dump_return
def find_user_by_id( id_usuario ):
    user = User.query.get( id_usuario )
    return user

@user_schema_dump_return
def insert_user( user ):
    db.session.add( user )
    db.session.commit()

    return user

def find_user_by_email( email ):
    user = User.query.filter( User.email == email ).first()
    return user
