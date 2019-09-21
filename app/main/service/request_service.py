from app.main import db
from app.main.model.request import Request
import datetime


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
    req = db.session.query(Request).filter(Request.id == data['event_id']).first()
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


def save_changes(changes):
    print("saving")
    db.session.add(changes)
    db.session.commit()
