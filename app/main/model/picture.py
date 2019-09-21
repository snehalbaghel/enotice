from .. import db


class Picture(db.Model):
    """
    Picture model to save event and user pictures
    """
    __tablename__ = 'picture'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=True, default=None)
    # data = db.Column(db.La)
