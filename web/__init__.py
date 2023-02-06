from flask import Flask
from web.dao.BaseDAO import BaseDAO
from web.dao.DbUtil import DbUtil
baseDAO = None
log = None


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object('config')

    # Initialize DbUtil
    db_util = DbUtil(app)
    global baseDAO
    baseDAO = BaseDAO(db_util)
    global log
    log = app.logger

    from web.routes.user import user_view
    app.register_blueprint(user_view, url_prefix='/')

    with app.app_context():
        log.info("app.app_context()")

    return app
