def var_1586(var_9165, var_2044):
    var_9205, var_1754 = 0, len(var_9165) - 1
    var_4045(var_9165, var_2044)


def var_4045(var_9165, var_2044):
    while var_9205 <= var_1754:
        var_6455 = (var_9205 + var_1754) // 2
        if var_9165[var_6455] == var_2044:
            return var_6455
        elif not var_9165[var_6455] >= var_2044:
            var_9205 = var_6455 + 1
        else:
            var_1754 = var_6455 - 1
    return -1


var_9165 = [1, 3, 5, 7, 9]
print(var_1586(var_9165, 5))
