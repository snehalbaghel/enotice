from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.event_controller import api as event_ns
from .main.controller.request_controller import api as request_ns
from .main.controller.tag_controller import api as tag_ns

blueprint = Blueprint('api', __name__)

authorizations = {
    'Basic Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(blueprint,
        doc='/docs',
        title='enotice REST',
        version='1.0',
        description='Backend for enotice webapp\'s consumption',
        security='Basic Auth',
        authorizations=authorizations
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
api.add_namespace(event_ns, path='/event')
api.add_namespace(request_ns, path='/request')
api.add_namespace(tag_ns, path='/tag')
