from app.main import db
from app.main.model.blacklist import BlacklistToken


def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        response = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response, 200
    except Exception as e:
        response = {
            'status': 'fail',
            'message': e
        }
        return response, 200
