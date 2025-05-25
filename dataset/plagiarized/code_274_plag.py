def var_5382(var_6820):
    if not var_6820 > 1:
        return var_6820
    sub_var_5382_1826(var_6820)


def sub_var_5382_1826(var_6820):
    var_1764, var_6575 = 0, 1
    var_5224 = 2
    while var_5224 < var_6820 + 1:
        var_1764, var_6575 = var_6575, var_1764 + var_6575
        var_5224 += 1
    return var_6575


print(var_5382(10))
