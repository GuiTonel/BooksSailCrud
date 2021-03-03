#Database_Model
from repository import db
class Book( db.Model ):
    def __init__( self, nome, autor ):
        super().__init__()
        self.nome = nome
        self.autor = autor

    __tablename__ = 'book'

    id = db.Column( db.Integer, primary_key = True )
    nome = db.Column( db.String( 255 ), nullable = False )
    autor = db.Column( db.String( 255 ), nullable = False )

#Schema
from flask_marshmallow import Marshmallow
class BookSchema( Marshmallow().SQLAlchemyAutoSchema ):
    class Meta():
        model = Book
