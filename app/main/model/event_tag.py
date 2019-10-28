from .. import db


class EventTag(db.Model):
    """
    Model to store various tags of events
    """
    __tablename__ = 'eventTag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
