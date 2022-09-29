from libs import *

def data_store(username, id, index):
    _USER_DIRECTORY = "users/"+str(username)
    _COMMANDS = [
        ""
    ]
    
    for _COMMAND in _COMMANDS:
        os.system(_COMMAND)