from app.main import db
from app.main.model.event import Event
from app.main.model.request import Request
import datetime
import dateutil.parser


def save_new_event(data):
    event_date = dateutil.parser.parse(data['time'])

    new_event = Event(
        title=data['title'],
        subtitle=data['subtitle'],
        description=data['description'],
        venue=data['venue'],
        time=event_date,
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
    events = Event.query.join(Request,
        Event.id == Request.event_id).filter(Request.status == 'pending').all()
    return events, 200


def get_published_events():
    events = Event.query.join(Request,
        Event.id == Request.event_id).filter(Request.status == 'approved').all()
    return events, 200


def get_event(id):
    return Event.query.join(Request,
        Event.id == Request.event_id).filter(Request.status == 'approved').filter(
        Event.id == id).first()


def save_changes(changes):
    print("saving")
    db.session.add(changes)
    db.session.commit()
