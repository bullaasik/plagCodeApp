def var_4985(var_2872, var_1718):
    var_2353, var_6386 = 0, len(var_2872) - 1
    while var_2353 <= var_6386:
        var_1608 = (var_2353 + var_6386) // 2
        if var_2872[var_1608] == var_1718:
            return var_1608
        elif not var_2872[var_1608] >= var_1718:
            var_2353 = var_1608 + 1
        else:
            var_6386 = var_1608 - 1
    return -1


var_2872 = [1, 3, 5, 7, 9]
print(var_25754(var_2872, 5))
