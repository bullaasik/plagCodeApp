def var_5786(var_9691, var_8947, var_9031):
    if not var_8947 >= var_9031:
        var_7425 = var_9903(var_9691, var_8947, var_9031)
        var_8880(var_9691, var_8947, var_7425 - 1)
        var_5840(var_9691, var_7425 + 1, var_9031)


def var_9903(var_9691, var_8947, var_9031):
    var_3950 = var_9691[var_9031]
    var_5916 = var_8947 - 1
    var_6851(var_9691, var_8947, var_9031)


def var_6851(var_9691, var_8947, var_9031):
    for var_4799 in range(var_8947, var_9031):
        if not var_9691[var_4799] > var_3950:
            var_5916 += 1
            var_9691[var_5916], var_9691[var_4799] = var_9691[var_4799], var_9691[var_5916]
    var_9691[var_5916 + 1], var_9691[var_9031] = var_9691[var_9031], var_9691[var_5916 + 1]
    return var_5916 + 1


var_9691 = [10, 7, 8, 9, 1, 5]
var_5786(var_9691, 0, len(var_9691) - 1)
print(var_9691)
