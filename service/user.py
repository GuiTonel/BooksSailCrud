from repository import user as user_repository

def find_users():
    return user_repository.find_users()

def find_user_by_id( id_usuario ):
    return user_repository.find_user_by_id( id_usuario )
    
def insert_user( user_json ):
    return user_repository.insert_user( user_json )