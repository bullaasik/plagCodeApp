def var_6424(var_5596):
    for var_6582 in range(1, len(var_5596)):
        var_4184 = var_5596[var_6582]
        var_3082 = var_6582 - 1
        while var_3082 >= 0 and var_5596[var_3082] > var_4184:
            var_5596[var_3082 + 1] = var_5596[var_3082]
            var_3082 -= 1
        var_5596[var_3082 + 1] = var_4184


var_5596 = [64, 34, 25, 12, 22, 11, 90]
var_6424(var_5596)
print(var_5596)
