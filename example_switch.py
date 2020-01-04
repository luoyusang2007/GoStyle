from gostyle import switch,case, default,  sw_set_var


a=4
outer_var="Switch"



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