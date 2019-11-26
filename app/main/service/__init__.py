from app.main import db


def save_changes(changes):
    print("saving")
    db.session.add(changes)
    db.session.commit()
