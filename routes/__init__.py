from .user import *
from .book import *

def init_routes( app ):
    app.register_blueprint( bp_user )
    app.register_blueprint( bp_book )
    