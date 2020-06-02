import os

from flask_sqlalchemy import SQLAlchemy

from flask import Flask


db = SQLAlchemy()

config = os.getenv('FLASK_CONFIG_MODULE', 'i_like_that.config.test')

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

with app.app_context():
    from . import views
    db.create_all() 
