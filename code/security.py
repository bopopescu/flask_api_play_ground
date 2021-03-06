from user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = User.find_by_username(username)  # if no user found return None
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity'][0]
    return User.find_by_user_id(user_id)
