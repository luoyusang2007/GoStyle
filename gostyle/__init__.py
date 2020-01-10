# gostyle
# Author: luoyusang2007(Sean Luo)
from ._go import go, to, Go, startable, destination
from ._defer import defer_inside, defer
from ._anonymous_func import func, af_set_var, af_get_var
from ._switch import sw_set_var, case, default, pass_break, switch