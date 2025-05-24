def var_8140(var_4277):
    var_4051 = 1
    var_6641(var_4277)


def var_6641(var_4277):
    var_3745 = 1
    while var_3745 < var_4277 + 1:
        var_4051 *= var_3745
        var_3745 += 1
    return var_4051


print(var_8140(5))
