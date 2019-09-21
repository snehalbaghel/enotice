from flask import request
from flask_restplus import Resource

from ..util.dto import RequestDto
from ..service.request_service import save_new_request, review_event
from ..util.decorator import token_required, admin_token_required
from app.main.service.auth_helper import Auth

api = RequestDto.api
_request = RequestDto.request


@api.route('/')
class Request(Resource):
    @api.doc('create new request')
    @api.response(201, 'Event successfully sent for review')
    @api.expect(_request, validate=True)
    @token_required
    def post(self):
        """Creates new request"""
        data = request.json
        return save_new_request(data=data)


@api.route('/review')
class RequestReview(Resource):
    @api.doc('review requests')
    @api.expect(_request)
    @admin_token_required
    def post(self):
        """Review requests"""
        data = request.json
        user, code = Auth.get_logged_in_user(request)
        data['user_id'] = user['data']['user_id']
        return review_event(data)
