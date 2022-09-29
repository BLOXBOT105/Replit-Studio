from modules import *
from libs import *

debug.enable()

_USERNAME = user = os.environ["REPL_OWNER"]


if check_user_value(_USERNAME):
    pass
else:
    new_user_event(_USERNAME)

debug.out("_DEBUG")

debug.disable()