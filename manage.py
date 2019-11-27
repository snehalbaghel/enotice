import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import url_for

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist, event, event_tag, tag, picture, request, review


app = create_app(os.getenv('EN_MODE') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    import os
    image_path = os.path.join(app.root_path, app.config.get('UPLOAD_FOLDER'))
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    app.run()


@manager.command
def test():
    """Runs unit tests"""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0

    return 1


if __name__ == '__main__':
    manager.run()
