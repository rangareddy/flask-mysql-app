"""
@author: rangareddy
@created: 05-Feb-2023
"""

from web.models.User import User


def get_user_by_dict(user_dict):
    user = None
    if user_dict:
        user = User(**user_dict)
    return user


class UserDAO:

    def __init__(self, dao):
        self.dao = dao
        self.table = "users"

    def get_all_users(self):
        users = self.dao.get_all("SELECT * FROM {}".format(self.table))
        all_users = []
        if users:
            for user_dict in users:
                all_users.append(get_user_by_dict(user_dict))
        return all_users

    def get_user(self, email, password):
        query = "SELECT * FROM {} WHERE email = '{}' AND password = '{}'".format(self.table, email, password)
        return self.get_user_by_query(query)

    def get_user_by_query(self, query):
        user_dict = self.dao.get(query)
        return get_user_by_dict(user_dict)

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM {} WHERE user_id = '{}'".format(self.table, user_id)
        return self.get_user_by_query(query)

    def get_user_by_email(self, email):
        query = "SELECT * FROM {} WHERE email = '{}'".format(self.table, email)
        return self.get_user_by_query(query)

    def create_user(self, user):
        admin = 1 if user.admin else 0
        query = "INSERT INTO {} (`first_name`, `last_name`, `email`, `password`, `admin`) " \
                "VALUES ('{}', '{}', '{}', '{}', '{}')".format(self.table, user.first_name, user.last_name, user.email,
                                                               user.password, admin)
        user = self.dao.insert(query)
        return user
