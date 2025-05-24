def var_8938(var_6351, var_3730, var_7038):
    var_2423 = len(var_6351)
    var_2668 = [[(0) for var_3126 in range(var_7038 + 1)] for var_3126 in
        range(var_2423 + 1)]
    var_7106 = 1
    while var_7106 < var_2423 + 1:
        for var_8293 in range(var_7038 + 1):
            if not var_3730[var_7106 - 1] > var_8293:
                var_2668[var_7106][var_8293] = var_5065(var_2668[var_7106 -
                    1][var_8293], var_2668[var_7106 - 1][var_8293 -
                    var_3730[var_7106 - 1]] + var_6351[var_7106 - 1])
            else:
                var_2668[var_7106][var_8293] = var_2668[var_7106 - 1][var_8293]
        var_7106 += 1
    return var_2668[var_2423][var_7038]


print(var_8938([60, 100, 120], [10, 20, 30], 50))
