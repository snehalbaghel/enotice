from flask import request
from flask_restplus import Resource

from ..util.dto import EventDto
from app.main.service.event_service import save_new_event, get_approved_events, get_pending_events
from app.main.util.decorator import token_required, admin_token_required
from app.main.service.auth_helper import Auth

api = EventDto.api
_event = EventDto.event


@api.route('/')
class Event(Resource):
    @api.response(201, 'Event successfully created.')
    # @api.doc(parser=parser)
    @api.doc('create new event')
    @api.expect(_event, validate=True)
    @token_required
    def post(self):
        """Creates a new event"""
        data = request.json
        user, code = Auth.get_logged_in_user(request)
        data['user_id'] = user['data']['user_id']
        return save_new_event(data)

    @api.doc('list of approved events')
    @api.marshal_list_with(_event, envelope='data')
    def get(self):
        """List of all approved events"""
        return get_approved_events()


@api.route('/pending')
class PendingEventList(Resource):
    @api.doc('list of pending events')
    @api.marshal_list_with(_event, envelope='data')
    @admin_token_required
    def get(self):
        """List of all pending events"""
        return get_pending_events()
