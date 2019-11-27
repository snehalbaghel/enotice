from app.main import db
from app.main.model.request import Request
import datetime
from . import save_changes


def save_new_request(data):
    new_request = Request(
        created_at=str(datetime.datetime.now()),
        event_id=data['event_id'],
        status='pending',
    )
    save_changes(new_request)
    response = {
        'status': 'Success',
        'message': 'Event successfully sent for review'
    }
    return response, 201


def review_event(data):
    req = Request.filter(Request.id == data['event_id']).one_or_none()
    if req:
        req.status = data['status']
        req.reviewed_by = data['user_id']
        req.remarks = data['remarks']
        print(req)
        db.session.commit()
        response = {
            'status': 'Success',
            'message': 'Successfully reviewed event'
        }
        return response, 200
    else:
        response = {
            'status': 'Failed',
            'message': 'Event id invalid'
        }
        return response, 400
