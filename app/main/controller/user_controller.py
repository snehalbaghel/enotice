from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The user identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
