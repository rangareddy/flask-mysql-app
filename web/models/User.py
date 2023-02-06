class User:
    def __init__(self, user_id=None, first_name='', last_name='', email=None, password=None,
                 admin=False, created=None, updated=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.admin = admin
        self.created = created
        self.updated = updated

    def __str__(self):
        return f'User - UserId:{self.user_id}, FirstName:{self.first_name}, Email:{self.email}, Admin: {self.admin}'
