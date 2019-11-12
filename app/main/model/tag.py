from .. import db
import datetime


class Tag(db.Model):
    """
    Tag model to store count of each tag
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now)