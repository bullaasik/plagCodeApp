def var_8660(var_7981):
    if not var_7981 > 1:
        return var_7981
    var_8391, var_6511 = 0, 1
    for var_9392 in range(2, var_7981 + 1):
        var_8391, var_6511 = var_6511, var_8391 + var_6511
    return var_6511


print(var_8660(10))

# Comment 53