from sets import Set
from flask_login import UserMixin

class User(UserMixin):

    username = ""
    is_admin = False

    def __init__(self, username, is_admin):
        self.username = username
        self.is_admin = is_admin     

    def __repr__(self):
        return "User(%s)" % (self.username)

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.username is other.username)
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

    def get_id(self):
        return self.username

    def is_admin(self):
        return self.is_admin

