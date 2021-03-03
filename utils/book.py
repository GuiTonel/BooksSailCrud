from models.book import BookSchema

book_schema = BookSchema()
books_schema = BookSchema( many = True )

def book_schema_dump_return( func ):
    def a( *args, **kwargs ):
        book = func( *args, **kwargs )

        if type( book ) == list:
            return books_schema.dumps( book )

        return book_schema.dump( book )
    return a
