from repository import db
from models.book import Book

from utils.book import book_schema_dump_return

@book_schema_dump_return
def find_books():
    books = Book.query.all()
    return books

@book_schema_dump_return
def find_book_by_id( id_usuario ):
    book = Book.query.get( id_usuario )
    return book

@book_schema_dump_return
def insert_book( book ):
    db.session.add( book )
    db.session.commit()

    return book
