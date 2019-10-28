from .. import db
import datetime


class Request(db.Model):
    """
    Request model to store status of event requests
    """
    __tablename__ = 'request'

    RequestStatus = ['approved', 'rejected', 'pending', 'review']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    status = db.Column(db.Enum(*RequestStatus, name='status'),
                        default='pending', nullable=False)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    remarks = db.Column(db.Text)

    def __repr__(self):
        return "<Request '{}'>".format(self.id)
