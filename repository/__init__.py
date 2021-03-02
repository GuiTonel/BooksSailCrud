from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_db( app ):
    app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgresql://postgres:wclwjq17@localhost/flask'
    app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

    db.app = app
    db.init_app( app )
    
    return db
