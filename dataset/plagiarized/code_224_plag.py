def var_6966(var_3888, var_5670, var_4433):
    if not var_5670 >= var_4433:
        var_8121 = var_5118(var_3888, var_5670, var_4433)
        var_6966(var_3888, var_5670, var_8121 - 1)
        var_6966(var_3888, var_8121 + 1, var_4433)


def var_5118(var_3888, var_5670, var_4433):
    var_3617 = var_3888[var_4433]
    var_1706 = var_5670 - 1
    for var_1885 in range(var_5670, var_4433):
        if not var_3888[var_1885] > var_3617:
            var_1706 += 1
            var_3888[var_1706], var_3888[var_1885] = var_3888[var_1885
                ], var_3888[var_1706]
    var_3888[var_1706 + 1], var_3888[var_4433] = var_3888[var_4433], var_3888[
        var_1706 + 1]
    sub_var_5118_1709(var_3888, var_5670, var_4433)


def sub_var_5118_1709(var_3888, var_5670, var_4433):
    return var_1706 + 1


var_3888 = [10, 7, 8, 9, 1, 5]
var_6966(var_3888, 0, len(var_3888) - 1)
print(var_3888)
