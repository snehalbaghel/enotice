from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(
            required=True,
            description='user\'s email address'),
        'username': fields.String(
            required=True,
            description='user\'s username'),
        'pubic_id': fields.String(description='user\'s public identifier'),
        'admin': fields.Boolean(description='is the user an admin')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })


class EventDto:
    api = Namespace('event', description='event related operations')
    event = api.model('event_details', {
        'title': fields.String(required=True, description='The event title'),
        'description': fields.String(required=True, description='The event description'),
        'venue': fields.String(required=True, description='The event venue'),
        'time': fields.String(required=True, description='The event time'),
        'link': fields.String(required=True, description='The event registration link')
    })


class RequestDto:
    api = Namespace('request', description='request related operations')
    request = api.model('request_details', {
        'event_id': fields.String(required=True,
                                description='The event id associated with the request'),
        'status': fields.String(required=False,
                                description='Status of request'),
        'remarks': fields.String(required=False,
                                description='Remarks for the event')
    })
