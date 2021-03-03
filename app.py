from flask import Flask

def init_app():
    #Database
    from repository import config_db
    app.db = config_db( app )

    from models import config_serializer
    config_serializer( app )

    app.db.create_all()


    #Rotas
    from routes import init_routes
    init_routes( app )

    app.run()

app = Flask(__name__)
init_app()
