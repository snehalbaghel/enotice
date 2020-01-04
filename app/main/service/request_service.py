from app.main import db
from app.main.model.request import Request
import datetime
from . import save_changes


def save_new_request(data):
    # TODO require token?
    response = {
        'event_id': data['event_id'],
    }

    try:
        new_request = Request(
        created_at=str(datetime.datetime.now()),
        event_id=int(data['event_id']),
        status='pending',)

        save_changes(new_request)

        response.status = 'success'
        response.message = 'event reviewed'
        response.code = 201
    except Exception as error:
        response.status = 'failure'
        response.message = str(error)
        response.code = 400

    return response


def review_event(data):
    req = Request.filter(Request.id == data['event_id']).one_or_none()

    response = {
        'event_id': data['event_id']
    }

    if req:
        req.status = 'review'
        req.reviewed_by = data['user_id']
        db.session.commit()
        response.status = 'success'
        response.message = 'reviewed event'
        return response
    else:
        response.status = 'failure'
        response.message = 'Event id invalid'

        return response
