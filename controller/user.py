from service import user as user_service

def find_users():
    return user_service.find_users()

def find_user_by_id( id_usuario ):
    return user_service.find_user_by_id( id_usuario )

def insert_user( user_json ):
    return user_service.insert_user( user_json )
    
