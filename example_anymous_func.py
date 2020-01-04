from gostyle import func,  af_set_var, af_get_var
b = func(
    lambda : af_set_var("ee", 3),
    lambda : print(af_get_var("ee") + 4)
)
b()