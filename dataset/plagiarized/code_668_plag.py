def var_7729(var_9856, var_1899):
    var_3810, var_2731 = 0, len(var_9856) - 1
    while var_3810 <= var_2731:
        var_2458 = (var_3810 + var_2731) // 2
        if var_9856[var_2458] == var_1899:
            return var_2458
        elif not var_9856[var_2458] >= var_1899:
            var_3810 = var_2458 + 1
        else:
            var_2731 = var_2458 - 1
    return -1


var_9856 = [1, 3, 5, 7, 9]
print(var_7729(var_9856, 5))
