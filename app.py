from flask_sqlalchemy import SQLAlchemy

from i_like_that import app, db


if __name__ == '__main__':
    from i_like_that.views import *
    app.run(host='0.0.0.0')