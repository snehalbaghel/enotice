from .. import db
import datetime


class Request(db.Model):
    """
    Request model to store status of event requests
    """

    RequestStatus = ['approved', 'rejected', 'pending', 'review']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    event = db.relationship("Event", backref=db.backref("request", uselist=False))
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    status = db.Column(db.Enum(*RequestStatus, name='status'),
                        default='pending', nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviewer = db.relationship("User")

    def __repr__(self):
        return "<Request '{}'>".format(self.id)
