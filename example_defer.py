from gostyle import defer_inside, defer
@defer_inside
def great_func():
    a = [1,2,3]
    b=8
    print("BEF")
    defer(
        lambda : a.append(7),
        lambda : print(a),
        lambda : print(b)
    )
    a[1] = 5 # Change content of a after claiming defer
    return a,b
    

print(great_func())
