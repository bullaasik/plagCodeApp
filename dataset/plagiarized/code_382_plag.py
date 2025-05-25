def var_1284(var_2792):
    if    not var_2792 > 1:
        return var_2792
    var_1740, var_8742 = 0, 1
    for var_5055 in range(2, var_2792 + 1):
        var_1740, var_8742 = var_8742, var_1740 + var_8742
    sub_var_1284_5762(var_2792)


def sub_var_1284_5762(var_2792):
    return var_8742


print(var_1284(10))
