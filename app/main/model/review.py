from .. import db
import datetime


class Review(db.Model):
    """
    Stores admin's feedback
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    request = db.relationship("Request", backref="reviews")
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviewer = db.relationship("User")
    review = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now,
                           onupdate=datetime.datetime.now)
