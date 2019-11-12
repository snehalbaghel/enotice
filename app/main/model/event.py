from .. import db
import datetime


class Event(db.Model):
    """
    Event model for storing event related details
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    subtitle = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text, nullable=False)
    venue = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", backref="events")
    picture_id = db.Column(db.Integer, db.ForeignKey('picture.id'),
                           default=None)
    link = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now,
                           onupdate=datetime.datetime.now)

    def __repr__(self):
        return "<Event '{}'>".format(self.id)
