def var_1010(var_9591):
    var_1625 = 1
    var_9718 = 1
    while var_9718 < var_9591 + 1:
        var_1625 *= var_9718
        var_9718 += 1
    var_6214(var_9591)


def var_6214(var_9591):
    return var_1625


print(var_1010(5))
