from .. import db
import datetime


class Picture(db.Model):
    """
    Picture model to save event and user pictures
    """

    id = db.Column(db.String(37), primary_key=True)
    description = db.Column(db.Text, nullable=True, default=None)
    filename = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)
