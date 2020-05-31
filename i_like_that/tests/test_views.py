import json
import os
import unittest

from flask_sqlalchemy import SQLAlchemy

from i_like_that.models import db
from i_like_that.views import app


class TestViews(unittest.TestCase):
    post_data = {
        'body': 'this is america'
    }

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_post(self):
        resp = self.app.post(
            '/posts/',
            data=json.dumps(self.post_data),
            content_type='application/json')
        data = json.loads(resp.data)

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['body'], self.post_data['body'])
