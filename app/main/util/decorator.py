from functools import wraps
from flask import request, g

from app.main.service.auth_helper import Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        g.current_user = token.user_id

        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response, 401

        g.current_user = token.data.user_id

        return f(*args, **kwargs)
    return decorated
