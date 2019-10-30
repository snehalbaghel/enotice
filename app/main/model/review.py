from .. import db


class Review(db.Model):
    """
    Stores admin's feedback
    """
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    review = db.Column(db.Text, nullable=False)
