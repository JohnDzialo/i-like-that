import json
import os
import unittest

from i_like_that import app, db


class TestViews(unittest.TestCase):
    post_data = {
        'body': 'this is america'
    }

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()

    def test_create_post(self):
        resp = self.app.post(
            '/posts/',
            data=json.dumps(self.post_data),
            content_type='application/json')
        data = json.loads(resp.data)

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['body'], self.post_data['body'])
