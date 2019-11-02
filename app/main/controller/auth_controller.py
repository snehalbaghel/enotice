from flask import request
from flask_restplus import Resource, marshal

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto, AuthResponseDto

api = AuthDto.api
user_auth = AuthDto.user_auth
auth_resp = AuthResponseDto.auth_response


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        resp, code = Auth.login_user(data=post_data)
        return marshal(resp, auth_resp), code


@api.route('/logout')
class LogoutAPI(Resource):
    """
        Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(auth_header)
