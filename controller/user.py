from service import user as user_service

def find_users():
    try:
        return user_service.find_users()
    except:
        return { 'error': 'falha ao buscar usuarios' }, 500   

def find_user_by_id( id_usuario ):
    return user_service.find_user_by_id( id_usuario )

def insert_user( user_json ):
    try:
        return user_service.insert_user( user_json )
    except:
        return { 'error': 'Falha ao inserir usuario' }, 500 
    
