from flask import Blueprint 

from controller import book as book_controller

bp_book = Blueprint( 'book', __name__, url_prefix = '/book' )

@bp_book.route( '/', methods = ['GET'] )
def get_books():
    return book_controller.find_books()
