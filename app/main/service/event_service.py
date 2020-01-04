from app.main import db
from app.main.model.event import Event
from app.main.model.request import Request
from app.main.model.tag import Tag
from app.main.model.event_tag import EventTag
from app.main.model.user import User
import datetime
import dateutil.parser
from . import save_changes


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
        picture_id=data['picture_id'],
    )

    add_tags(data['tags'], new_event.id)
    save_changes(new_event)

    response = {
        'status': 'success',
        'message': 'Successfully created event'
    }

    return response, 201


def get_pending_events():
    events = db.session.query(Event, Request, User).join(Request,
        Event.id == Request.event_id).add_columns().filter(Request.status.in_(['pending', 'review'])).filter(
            Event.user_id == User.id).all()
    print(events, "Hello")
    return events, 200


def get_published_events():
    events = Event.query.join(Request,
        Event.id == Request.event_id).filter(Request.status == 'approved').all()
    return events, 200


def get_event(id):
    return Event.query.join(Request,
        Event.id == Request.event_id).filter(Request.status == 'approved').filter(
        Event.id == id).first()


def add_tags(tags, eventId):
    for tag in tags:
        existing_tag = Tag.query.filter(Tag.name == tag).first()

        if (not existing_tag):
            existing_tag = Tag(name=tag)
            save_changes(existing_tag)

        new_event_tag = EventTag(
            event_id=eventId,
            tag_id=existing_tag.id
        )
        existing_tag.count += 1
        save_changes(new_event_tag)
