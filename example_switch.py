from gostyle.switch import switch,case, default, set_var as sw_set_var
from gostyle.anonymous_func import func, set_var as af_set_var, get_var as af_get_var

a=4
outer_var="Switch"


b = func(
    lambda : af_set_var("ee", 3),
    lambda : print(af_get_var("ee") + 4)
)


# Return and 
switch(a,{
    case(3):(
        lambda : print(outer_var + "3")
    ),
    case(4):(
        lambda : print(outer_var + "04"),
        lambda : sw_set_var("outer_var", "SSSSSSwitch"),
        lambda : print(outer_var + "4"),
        lambda : print(outer_var + "44")
    ),
    default:(
        lambda : print("default")
    )
})

print(outer_var)