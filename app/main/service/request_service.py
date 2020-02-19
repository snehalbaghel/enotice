from app.main import db
from app.main.model.request import Request
from app.main.model.review import Review
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

        response['status'] = 'success'
        response['message'] = 'Request sent.'
        response['code'] = 201
    except Exception as error:
        response['status'] = 'failure'
        response['message'] = str(error)
        response['code'] = 400

    return response


def review_event(data, reviewer_id):
    req = Request.query.filter(Request.id == data['request_id']).one_or_none()
    response = {
        'request_id': data['request_id']
    }

    if req:
        if data['status'] == 'review':
            req.status = 'review'
            review = Review(request_id=req.id,
                reviewer_id=reviewer_id,
                review=data['review_msg'])
            save_changes(review)

            response['status'] = 'success'
            response['message'] = 'Reviewed event'
            return response
        elif data['status'] == 'approved':
            req.status = 'approved'
            req.reviewer_id = reviewer_id
            db.session.commit()

            response['status'] = 'success'
            response['message'] = 'Approved event'
            return response

    response['status'] = 'failure'
    response['message'] = 'Event id invalid'

    return response
