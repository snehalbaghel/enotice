import uuid

from app.main import db
from app.main.model.user import User
from app.main.model.event import Event

# TODO: Add logout event


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
        return generate_token(new_user)
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


def get_user_events(user):
    return Event.query.filter_by(user_id=user).all()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response = {
            'status': 'success',
            'message': 'Successfully registered',
            'Authorization': auth_token.decode()
        }
        return response, 201
    except Exception as e:
        print(e)
        response = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response, 401


def save_changes(changes):
    print("saving")
    db.session.add(changes)
    db.session.commit()
