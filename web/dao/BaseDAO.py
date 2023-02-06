"""
@author: rangareddy
@created: 05-Feb-2023
"""

import logging

log = logging.getLogger(__name__)


class BaseDAO:

    def __init__(self, dbutil):
        self.dbutil = dbutil

    def get_all(self, query):
        log.debug(" Executing get_all() with query " + query)
        q = self.dbutil.query(query)
        return q.fetchall()

    def get(self, query):
        log.debug(" Executing get() with query " + query)
        q = self.dbutil.query(query)
        return q.fetchone()

    def execute_query(self, query):
        try:
            dbutil = self.dbutil
            dbutil.query(query)
            dbutil.commit()
            return True
        except:
            dbutil.rollback()
            return False

    def insert(self, query):
        log.debug(" Executing insert query - " + query)
        self.execute_query(query)

    def update(self, query):
        log.debug(" Executing update query - " + query)
        self.execute_query(query)

    def delete(self, query):
        log.debug(" Executing delete query - " + query)
        self.execute_query(query)
