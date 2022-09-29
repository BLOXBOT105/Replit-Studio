from libs import *

def check_user_value(username):
    _USER_DIRECTORY = "users/"+str(username)
    return os.path.isdir(_USER_DIRECTORY)