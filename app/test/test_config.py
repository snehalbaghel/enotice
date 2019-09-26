import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app


class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevConfig')
        return app

    def test_app_is_dev(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'pls_put_secret_key')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'mysql+pymysql://root:student@localhost/enotice'
        )


class TestTestConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestConfig')
        return app

    def test_app_is_test(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'mysql+pymysql://root:student@localhost/enotice'
        )
