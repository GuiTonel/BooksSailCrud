from service import user as user_service

from models.user import UserSchema

PASSWORD = "password"
EMAIL = "email"

def find_users():
    try:
        return user_service.find_users()
    except:
        return { 'error': 'falha ao buscar usuarios' }, 500   

def find_user_by_id( id_usuario ):
    return user_service.find_user_by_id( id_usuario )

def insert_user( user_json ):
    user = UserSchema().load( user_json )
    try:
        user.password = user_service.set_user_password( user.password )
        return user_service.insert_user( user )
    except Exception as e:
        print(e)
        return { 'error': 'Falha ao inserir usuario' }, 500 
    
def login( user_json ):
    password = user_json[ PASSWORD ]
    email = user_json[ EMAIL ]

    try:
        user = user_service.login( email, password )
        return user
            
    except Exception as e:
        return { "error": str( e ) }, 500
