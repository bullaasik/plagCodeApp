def var_3563(var_6423, var_2093, var_6741):
    if not var_2093 >= var_6741:
        var_4703 = var_6651(var_6423, var_2093, var_6741)
        var_3563(var_6423, var_2093, var_4703 - 1)
        var_3563(var_6423, var_4703 + 1, var_6741)


def var_6651(var_6423, var_2093, var_6741):
    var_2551 = var_6423[var_6741]
    var_2001 = var_2093 - 1
    for var_8679 in range(var_2093, var_6741):
        if not var_6423[var_8679] > var_2551:
            var_2001 += 1
            var_6423[var_2001], var_6423[var_8679] = var_6423[var_8679], var_6423[var_2001]
    var_6423[var_2001 + 1], var_6423[var_6741] = var_6423[var_6741], var_6423[var_2001 + 1]
    return var_2001 + 1


var_6423 = [10, 7, 8, 9, 1, 5]
var_3563(var_6423, 0, len(var_6423) - 1)
print(var_6423)
