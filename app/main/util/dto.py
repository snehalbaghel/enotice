from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'public_id': fields.String(description='user\'s public identifier'),
        'email': fields.String(
            required=True,
            description='user\'s email address'),
        'username': fields.String(
            required=True,
            description='user\'s username'),
        'admin': fields.Boolean(description='is the user an admin')
    })


#  TODO: Add auth response model here
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })


class EventDto:
    api = Namespace('event', description='event related operations')
    event = api.model('event_details', {
        'id': fields.String(description='event\'s id'),
        'title': fields.String(required=True, description='The event title'),
        'subtitle': fields.String(required=True, description='The event subtitle'),
        'description': fields.String(required=True, description='The event description'),
        'venue': fields.String(required=True, description='The event venue'),
        'time': fields.DateTime(required=True, description='The event time'),
        'link': fields.String(required=True, description='The event registration link'),
        'picture_id': fields.String(required=False, description='The picture\'s primary key'),
        'tags': fields.List(fields.String(required=True, description='Tag\'s associated with the event'))
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


class AuthResponseDto:
    api = Namespace('auth', description='auth response')
    auth_response = api.model('auth_response', {
        'status': fields.String(required=True,
                                description='success/failure of request'),
        'message': fields.String(required=True, description='additional info'),
        'Authorization': fields.String(required=False, description='jwt token'),
        'user': fields.Nested(UserDto.user, required=False, description='user profile')
    })


class TagDto:
    api = Namespace('tag', description='tags related operations')
    tag_response = api.model('tag_response', {
        'id': fields.String(required=True, description='Id of tag'),
        'name': fields.String(required=True, description='Name of the tag'),
        'count': fields.String(required=True, description='No. of events with this tag')
    })
