from libs import *
class LocalPlayer:
    _PATH = "users/"+str(os.environ["REPL_OWNER"])
    _IMPORT_PATH = "users."+str(os.environ["REPL_OWNER"])
    _USER_MODULES = __import__(_IMPORT_PATH+".user_modules")
 
    Name = str(os.environ["REPL_OWNER"])
    GameData = __import__(_IMPORT_PATH+".user_modules.data_store")