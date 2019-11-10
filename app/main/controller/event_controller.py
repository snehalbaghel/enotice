from flask import request, g
from flask_restplus import Resource

from ..util.dto import EventDto
from app.main.service.event_service import save_new_event, get_published_events, get_pending_events, get_event
from app.main.util.decorator import token_required, admin_token_required
from app.main.service.auth_helper import Auth

api = EventDto.api
_event = EventDto.event


@api.route('/')
class EventList(Resource):
    @api.response(201, 'Event successfully created.')
    # @api.doc(parser=parser)
    @api.doc('create new event')
    @api.expect(_event, validate=True)
    @token_required
    def post(self):
        """Creates a new event"""
        data = request.json
        data['user_id'] = g.current_user
        return save_new_event(data)


@api.route('/<id>')
@api.param('id', 'The event identifier')
@api.response(404, 'Event not found.')
class Event(Resource):
    @api.doc('get event(published) details from it\'s id')
    @api.marshal_with(_event)
    def get(self, id):
        """Get event details from it\'s id"""
        event = get_event(id)
        if not event:
            api.abort(404)
        else:
            return event


@api.route('/pending')
class PendingEventsList(Resource):
    @api.doc('list of pending events (admin function)')
    @api.marshal_list_with(_event)
    @admin_token_required
    def get(self):
        """List of all pending events (admin function)"""
        return get_pending_events()


@api.route('/published')
class PublishedEventsList(Resource):
    @api.doc('list of published events')
    @api.marshal_list_with(_event)
    def get(self):
        """List of all published events"""
        return get_published_events()
