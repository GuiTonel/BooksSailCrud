from flask_marshmallow import Marshmallow

from .book import Book
from .user import User

ma = Marshmallow()
def config_serializer ( app ):
    ma.init_app( app )
