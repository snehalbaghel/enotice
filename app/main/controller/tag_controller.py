from flask_restx import Resource

from ..util.dto import TagDto
from ..model.tag import Tag


api = TagDto.api
tag_response = TagDto.tag_response


@api.route('/all')
class TagList(Resource):
    @api.doc('list of all tags')
    @api.marshal_list_with(tag_response)
    def get(self):
        """List of all tags in all events"""
        return Tag.query.all()
