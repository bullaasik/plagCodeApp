def var_4338(var_8362, var_2235):
    var_8658, var_8649 = 0, len(var_8362) - 1
    while var_8658 <= var_8649:
        var_4577 = (var_8658 + var_8649) // 2
        if var_8362[var_4577] == var_2235:
            return var_4577
        elif not var_8362[var_4577] >= var_2235:
            var_8658 = var_4577 + 1
        else:
            var_8649 = var_4577 - 1
    return -1


var_8362 = [1, 3, 5, 7, 9]
print(var_4338(var_8362, 5))
