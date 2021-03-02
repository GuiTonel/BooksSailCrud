from flask_marshmallow import Marshmallow

ma = Marshmallow()
def config_serializer ( app ):
    ma.init_app( app )
