from libs import *

def new_user_event(username):
    _USER_DIRECTORY = "users/"+str(username)
    _COMMANDS = [
        "cp -a default_user "+_USER_DIRECTORY
    ]
    
    for _COMMAND in _COMMANDS:
        os.system(_COMMAND)