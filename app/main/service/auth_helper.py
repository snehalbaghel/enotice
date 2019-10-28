from app.main.model.user import User
from ..service.blacklist_service import save_token


class Auth:
    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response, 200
            else:
                response = {
                    'status': 'fail',
                    'message': 'email or password does not match'
                }
                return response, 401
        except Exception as e:
            print(e)
            response = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return save_token(token=auth_token)
            else:
                response = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization').split(" ")[1]
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin
                    }
                }
                return response, 200
        else:
            response = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response, 401
