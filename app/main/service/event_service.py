from app.main import db
from app.main.model.event import Event
from app.main.model.request import Request
import datetime


def save_new_event(data):
    new_event = Event(
        title=data['title'],
        subtitle=data['subtitle'],
        description=data['description'],
        venue=data['venue'],
        time=data['time'],
        user_id=data['user_id'],
        link=data['link'],
    )
    save_changes(new_event)

    response = {
        'status': 'success',
        'message': 'Successfully created event'
    }

    return response, 201


def get_pending_events():
    events = Event.query.join(Request).filter(Request.status == 'pending')
    return events, 200


def get_published_events():
    events = Event.query.join(Request).filter(Request.status == 'approved')
    return events, 200


def get_event(id):
    # TODO: return only published event
    return Event.query.filter_by(id=id).first()

# def get_active_events():
    # events = Event.query.
    # pass


def save_changes(changes):
    print("saving")
    db.session.add(changes)
    db.session.commit()
