def var_4678(var_5979):
    if not var_5979 > 1:
        return var_5979
    var_9095(var_5979)


def var_9095(var_5979):
    var_8593, var_5947 = 0, 1
    var_1691 = 2
    while var_1691 < var_5979 + 1:
        var_8593, var_5947 = var_5947, var_8593 + var_5947
        var_1691 += 1
    return var_5947


print(var_4678(10))
