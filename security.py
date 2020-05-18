# safe_str_cmp is imported from werkzeug to compare strings
from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    user = User.find_by_username(username) #here we created a new method without mapping
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    userid = payload['identity']
    return User.find_by_id(user_id) # here we changed the line according to the ID search
