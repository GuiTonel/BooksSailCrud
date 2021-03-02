from models.user import UserSchema

user_schema = UserSchema()
def user_schema_dump_return( func ):
    def a( *args ):
        return user_schema.dump( func( args[0] ) )
    return a

users_schema = UserSchema( many = True )
def users_schema_dump_return( func ):
    def a():
        return users_schema.dumps( func() )
    return a