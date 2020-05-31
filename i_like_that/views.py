import os

from flask import jsonify, request

from .models import db, Post
from i_like_that import app


@app.route('/posts/', methods=['POST'])
def create_post():
    post = Post.from_json(request.json)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post_by_id(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify(post.to_json())


@app.route('/posts/<int:id>')
def get_post_by_id(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())


@app.route('/posts/')
def get_posts():
    posts = Post.query.all()
    return jsonify({
        'posts': [post.to_json() for post in posts],
    })


@app.route('/posts/<int:id>/likeit/<up_or_down>/', methods=['PUT'])
def like_post(id, up_or_down):
    post = Post.query.get_or_404(id)
    if up_or_down == 'up':
        post.likes += 1
    if up_or_down == 'down':
        post.likes -= 1
    db.session.commit()
    return jsonify(post.to_json())
