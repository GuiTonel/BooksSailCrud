#Database_Model
from repository import db
class Book( db.Model ):
    __tablename__ = 'book'

    id = db.Column( db.Integer, primary_key = True )
    nome = db.Column( db.String( 255 ), nullable = False )
    autor = db.Column( db.String( 255 ), nullable = False )

#Schema
from flask_marshmallow import Marshmallow
from marshmallow import post_load
class BookSchema( Marshmallow().SQLAlchemyAutoSchema ):
    class Meta():
        model = Book

    @post_load
    def make_book(self, data, **kwargs):
        return Book(**data)
