from service import book as book_service
from models.book import BookSchema

def find_books():
    return book_service.find_books()

def find_book_by_id( id_usuario ):
    return book_service.find_book_by_id( id_usuario )
    
def insert_book( book_json ):
    book = BookSchema().load( book_json )
    return book_service.insert_book( book )
    