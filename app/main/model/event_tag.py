from .. import db
import datetime


class EventTag(db.Model):
    """
    Model to store various tags of events
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
