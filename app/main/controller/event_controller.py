from flask import request, g
from flask_restplus import Resource
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from ..util.dto import EventDto
from app.main.service.event_service import save_new_event, get_published_events, get_pending_events, get_event
from app.main.util.decorator import token_required, admin_token_required
from app.main.service.auth_helper import Auth
from app.main.model.picture import Picture
from app.main.service import save_changes
from flask import current_app


api = EventDto.api
_event = EventDto.event

upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                            type=FileStorage, required=True, help='image file')


@api.route('/')
class EventList(Resource):
    @api.response(201, 'Event successfully created.')
    # @api.doc(parser=parser)
    @api.doc('create new event')
    @api.expect(_event, validate=True)
    @token_required
    def post(self):
        """Creates a new event"""
        data = request.json
        data['user_id'] = g.current_user
        return save_new_event(data)


@api.route('/<id>')
@api.param('id', 'The event identifier')
@api.response(404, 'Event not found.')
class Event(Resource):
    @api.doc('get event(published) details from it\'s id')
    @api.marshal_with(_event)
    def get(self, id):
        """Get event details from it\'s id"""
        event = get_event(id)
        if not event:
            api.abort(404)
        else:
            return event


@api.route('/pending')
class PendingEventsList(Resource):
    @api.doc('list of pending events (admin function)')
    @api.marshal_list_with(_event)
    @admin_token_required
    def get(self):
        """List of all pending events (admin function)"""
        return get_pending_events()


@api.route('/published')
class PublishedEventsList(Resource):
    @api.doc('list of published events')
    @api.marshal_list_with(_event)
    def get(self):
        """List of all published events"""
        return get_published_events()


@api.route('/image')
class PosterImage(Resource):
    @api.doc('upload endpoint for image')
    @api.expect(upload_parser)
    @api.marshal_with(EventDto.upload_response)
    def post(self):
        """Endpoint to upload an image file"""
        args = upload_parser.parse_args()
        upload_file = args['file']
        try:
            print(upload_file.mimetype)
            if 'image/' in upload_file.mimetype:
                import os
                import uuid

                file_ext = secure_filename(upload_file.filename)
                file_name = str(uuid.uuid4()) + file_ext
                public_id = str(uuid.uuid4())
                destination = os.path.join(current_app.root_path, current_app.config.get('UPLOAD_FOLDER'))

                upload_file.save(os.path.join(destination, file_name))

                new_pic = Picture(id=public_id, filename=file_name)

                save_changes(new_pic)

                response = {
                    'status': 'success',
                    'picture_id': public_id
                }

                return response, 200
            else:
                raise Exception('File is not an image')
        except Exception as e:
            print(e)
            response = {
                'status': 'failed'
            }
            return response, 200
