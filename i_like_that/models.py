from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy

from i_like_that import db
from i_like_that.exceptions import ValidationError


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    likes = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True,
                          default=datetime.now(timezone.utc))

    def to_json(self):
        json_post = {
            'id': self.id,
            'body': self.body,
            'likes': self.likes,
            'timestamp': self.timestamp
        }
        return json_post

    @staticmethod
    def from_json(json_post):
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('post does not have a body')
        return Post(body=body)


db.create_all()
db.session.commit()