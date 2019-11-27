from flask import request, g
from flask_restplus import Resource

from ..util.dto import RequestDto
from ..service.request_service import save_new_request, review_event
from ..util.decorator import token_required, admin_token_required
from ..model.event import Event
from ..model.request import Request as RequestModel
from ..model.review import Review

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
        data['user_id'] = g.current_user
        return review_event(data)


@api.route('/history/<id>')
class ReviewHistory(Resource):
    @api.doc('get event\'s review history')
    @api.param('id', description='Event\'s id')
    @token_required
    @api.marshal_with(RequestDto.history)
    def get(self, id):
        """Event\'s review history"""
        event = Event.query.filter(Event.id == id).one_or_none()

        if (event and event.user_id == g.current_user):
            timeline = list()
            print(event)
            timeline.append({
                'actor': 'You',
                'datetime': event.created_at,
                'message': 'Created event'
            })

            request = RequestModel.query.filter(RequestModel.event_id == id).one_or_none()

            if (request):
                timeline.append({
                    'actor': 'You',
                    'datetime': request.created_at,
                    'message': 'Submitted for approval'
                })

                reviews = Review.query.filter(Review.request_id == request.id).all()

                if (reviews):
                    for review in reviews:
                        timeline.append({
                            'actor': 'Admin',
                            'datetime': review.created_at,
                            'message': review.review
                        })

                if(request.status in ['approved', 'rejected']):
                    timeline.append({
                        'actor': 'Admin',
                        'datetime': request.updated_at,
                        'message': 'Event approved' if request.status == 'approved' else 'Event Rejected'
                    })

            response = {
                'status': 'success',
                'current_status': request.status if request else 'NA',
                'timeline': timeline
            }

            return response, 200
        else:
            response = {
                'status': 'failed',
                'message': 'Invalid user or event id'
            }

            return response, 400
