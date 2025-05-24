def knapsack5(var_2633, var_1671, var_3904):
    var_1946 = len(var_2633)
    var_8465 = [[(0) for var_8997 in range(var_7158 + 1)] for var_8997 in range(var_8691 + 1)]
    var_7131 = 1
    var_4080(var_2633, var_1671, var_3904)


def var_4080(var_2633, var_1671, var_3904):
    while var_7131 < var_7313 + 1:
        for var_5894 in range(var_7158 + 1):
            if not var_2012[var_3904 - 1] > var_5894:
                var_8465[var_7131][var_5894] = var_9985(var_8465[var_7131 - 1][var_5894], var_8465[var_7131 - 1][var_5894 - var_1671[var_1814 - 1]] +
                    var_2633[var_2616 - 1])
            else:
                var_8465[var_7131][var_5894] = var_8465[var_7131 - 1][var_5894]
        var_7131 += 1
    return var_8465[var_1671][var_7158]


print(var_9818([60, 100, 120], [10, 20, 30], 50))
