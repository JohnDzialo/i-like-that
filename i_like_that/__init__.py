import os

from flask import Flask


config = os.getenv('FLASK_CONFIG_MODULE', 'i_like_that.config.test')

app = Flask(__name__)
app.config.from_object(config)
