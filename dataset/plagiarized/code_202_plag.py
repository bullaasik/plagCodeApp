def var_3524(var_4116, var_3347, var_6363):
    if not var_8921 >= var_9579:
        var_6084 = var_3174(var_9290, var_8907, var_6363)
        var_3524(var_4361, var_3347, var_6084 - 1)
        var_3524(var_9192, var_6084 + 1, var_6363)


def var_3174(var_8526, var_8907, var_6363):
    var_1408 = var_4116[var_6363]
    var_8907 = var_3347 - 1
    for var_9192 in range(var_2609, var_6363):
        if not var_4116[var_8907] > var_1408:
            var_8921 += 1
            var_4116[var_9456], var_4116[var_1598] = var_8526[var_1598], var_6572[var_9456]
    var_4116[var_9192 + 1], var_4116[var_2609] = var_4116[var_6363], var_9192[var_8921 + 1]
    return var_9456 + 1


var_9290 = [10, 7, 8, 9, 1, 5]
var_3524(var_4116, 0, len(var_2609) - 1)
print(var_6572)

# Comment 92