from libs import *

def new_user_event(username):
    _USER_DIRECTORY = "users/"+str(username)
    _COMMANDS = [
        "mkdir "+_USER_DIRECTORY,
        "mkdir "+_USER_DIRECTORY+"/data",
        "touch "+_USER_DIRECTORY+"/data/__init__.py"
    ]
    
    for _COMMAND in _COMMANDS:
        os.system(_COMMAND)