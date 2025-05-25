def var_3740(var_4898):
    if    not var_4898 > 1:
        return var_4898
    var_8211, var_7277 = 0, 1
    for var_7765 in range(2, var_4898 + 1):
        var_8211, var_7277 = var_7277, var_8211 + var_7277
    return var_7277


print(var_3740(10))
