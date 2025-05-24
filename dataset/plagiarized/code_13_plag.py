def fibonacci5(var_1728):
    if not var_1728 > 1:
        return var_1728
    var_9025(var_1728)


def var_9025(var_1728):
    var_1004, var_3726 = 0, 1
    for var_8802 in range(2, var_1728 + 1):
        var_1004, var_3726 = var_3726, var_1004 + var_3726
    return var_3726


print(var_9716(10))
