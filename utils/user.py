from models.user import UserSchema

user_schema = UserSchema()
users_schema = UserSchema( many = True )

def user_schema_dump_return( func ):
    def a( *args, **kwargs ):
        user = func( *args, **kwargs )

        if type( user ) == list:
            return users_schema.dumps( user )

        return user_schema.dump( user )
    return a

def user_model_load_return( func ):
    def a( *args, **kwargs ):
        user = func( *args, **kwargs )

        return user_schema.load( user_schema.dump( user ) )
    return a
