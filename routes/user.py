from flask import request

from controller import user as user_controller

from flask import Blueprint, request
bp_user = Blueprint( 'user', __name__, url_prefix = '/user' )

@bp_user.route( '/', methods = ['GET'] )
def get_users():
    return user_controller.find_users()

@bp_user.route( '/<int:id_usuario>', methods = ['GET'] )
def get_user_by_id( id_usuario ):
    return user_controller.find_user_by_id( id_usuario )

@bp_user.route( '/cadastrar', methods = ['POST'] )
def insert_user():
    return user_controller.insert_user( request.get_json() )

@bp_user.route( '/login', methods = ['GET'] )
def login():
    return user_controller.login( request.get_json() )
