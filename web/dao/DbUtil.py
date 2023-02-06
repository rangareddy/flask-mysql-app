"""
@author: rangareddy
@created: 05-Feb-2023
"""

import MySQLdb
from flask_mysqldb import MySQL
import logging


class DbUtil:
    log = logging.getLogger(__name__)

    def __init__(self, app):
        logging.info("Initializing the MYSQL")
        self.mysql = MySQL(app)
        self.conn = self.mysql.connection

    def cursor(self):
        return self.conn.cursor(MySQLdb.cursors.DictCursor)

    def query(self, query):
        cur = self.cursor()
        cur.execute(query)
        return cur

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()
