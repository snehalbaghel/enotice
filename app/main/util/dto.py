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
    })
    upload_response = api.model('upload_response', {
        'status': fields.String(description='success/fail'),
        'picture_id': fields.String(description='picture\'s public id', required=False)
    })
    pending_events_response = api.model('pending_events_response', {
        'request_id': fields.String(description='request\'s id', required=True, attribute="request.id"),
        'title': fields.String(description='event title', required=True, attribute="event.title"),
        'username': fields.String(description='requester\'s username', required=True, attribute="user.username"),
        'event_date': fields.DateTime(description='event\'s date', required=True, attribute="event.time"),
        'request_date': fields.DateTime(description='request created_at', required=True,
        attribute="request.created_at"),
        'current_status': fields.String(description='request\'s status', required=True, attribute="request.status"),
    })


class RequestDto:
    api = Namespace('request', description='request related operations')
    request = api.model('request_details', {
        'event_id': fields.String(required=True,
                                description='The event id associated with the request'),
        'status': fields.String(required=False, description='In case of approval req'),
    })
    timeline_item = api.model('timeline_item', {
        'actor': fields.String(description='The actor of the item'),
        'datetime': fields.DateTime(description='Time when event occurred'),
        'message': fields.String(description='Description of the event/feedback')
    })

    history = api.model('request_history', {
        'current_status': fields.String(required=False, description='The current status of the request'),
        'timeline': fields.List(fields.Nested(timeline_item), description='History of the request', required=False),
        'status': fields.String(required=False, description='status of request'),
        'message': fields.String(request=False, description='error message if failed')
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
