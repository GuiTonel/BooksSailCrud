from .user import bp_user as user_routes

from .user import *

def init_routes( app ):
    app.register_blueprint( user_routes )
    