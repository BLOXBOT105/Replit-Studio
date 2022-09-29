from modules import *
from libs import *

debug.enable()

_USERNAME = os.environ["REPL_OWNER"]


if check_user_value(_USERNAME):
    pass
else:
    new_user_event(_USERNAME)

from users import *

debug.out(LocalPlayer.Name)

debug.disable()