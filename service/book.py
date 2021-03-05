from repository import book as book_repository

def find_books():
    return book_repository.find_books()

def find_book_by_id( id_usuario ):
    return book_repository.find_book_by_id( id_usuario )
    
def insert_book( book ):
    return book_repository.insert_book( book )
