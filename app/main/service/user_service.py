import uuid

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    print(user)
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
        )
        save_changes(new_user)
        response = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response, 409


def get_all_users():
    return User.query.all()


def get_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(changes):
    print("saving")
    db.session.add(changes)
    db.session.commit()
