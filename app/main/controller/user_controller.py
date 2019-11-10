from flask import request, g
from flask_restplus import Resource

from ..util.dto import UserDto, EventDto, RequestDto
from ..service.user_service import save_new_user, get_all_users, get_user, get_user_events
from ..util.decorator import token_required

api = UserDto.api
_user = UserDto.user
_event = EventDto.event


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
        """Get a user given its identifier"""
        user = get_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/events')
class Events(Resource):
    @api.doc('get user\'s saved events')
    @api.marshal_list_with(_event)
    @token_required
    def get(self):
        """Get user\'s saved events"""
        return get_user_events(g.current_user)


# @api.route('/requests')
# class Request(Resource):
    # @api.doc('get user\'s requests')
    # @api.marshal_list_with()
    # @token_required
    # def get(self):
        # """Get user\'s requests"""
        # return {}
