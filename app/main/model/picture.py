from .. import db
import datetime


class Picture(db.Model):
    """
    Picture model to save event and user pictures
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=True, default=None)
    path = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
