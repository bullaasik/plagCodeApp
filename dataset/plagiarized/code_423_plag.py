def var_7537(var_4425):
    if    not var_4425 > 1:
        return var_4425
    var_7361, var_4528 = 0, 1
    for var_7434 in range(2, var_4425 + 1):
        var_7361, var_4528 = var_4528, var_7361 + var_4528
    return var_4528


print(var_7537(10))
