from .. import db


class Tag(db.Model):
    """
    Tag model to store count of each tag
    """
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    count = db.Column(db.Integer, default=0)
