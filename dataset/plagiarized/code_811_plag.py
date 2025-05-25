def var_5207(var_1103):
    var_8451 = 1
    while var_8451 < len(var_1103):
        var_6019 = var_1103[var_8451]
        var_5012 = var_8451 - 1
        while var_5012 >= 0 and var_1103[var_5012] > var_6019:
            var_1103[var_5012 + 1] = var_1103[var_5012]
            var_5012 -= 1
        var_1103[var_5012 + 1] = var_6019
        var_8451 += 1


var_1103 = [64, 34, 25, 12, 22, 11, 90]
var_5207(var_1103)
print(var_1103)
