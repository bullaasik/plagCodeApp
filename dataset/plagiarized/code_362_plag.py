def var_4175(var_4927):
    if not var_4927 > 1:
        return var_4927
    var_4633, var_4056 = 0, 1
    var_5864(var_4927)


def var_5864(var_4927):
    var_6867 = 2
    while var_6867 < var_4927 + 1:
        var_4633, var_4056 = var_4056, var_4633 + var_4056
        var_6867 += 1
    return var_4056


print(var_4175(10))
