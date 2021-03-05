from werkzeug.security import generate_password_hash, check_password_hash

from repository import user as user_repository
from models.user import UserSchema

def find_users():
    return user_repository.find_users()

def find_user_by_id( id_usuario ):
    return user_repository.find_user_by_id( id_usuario )
    
def insert_user( user ):
    return user_repository.insert_user( user )

def set_user_password( password ):
    return generate_password_hash( password )

def validate_user_password( password, password_hash ):
    return check_password_hash( password_hash, password )

def get_user_by_email( email ):
    return user_repository.find_user_by_email( email )

def login( email, password ):
    user = get_user_by_email( email )

    if validate_user_password( password, user.password ):
        user.password = None
        return UserSchema().dump( user ), 200

    else:
        raise Exception("Senha incorreta!")
