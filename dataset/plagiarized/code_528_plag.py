def var_8596(var_6314):
    var_7606 = 1
    while var_7606 < len(var_6314):
        var_8608 = var_6314[var_7606]
        var_8408 = var_7606 - 1
        while var_8408 >= 0 and var_6314[var_8408] > var_8608:
            var_6314[var_8408 + 1] = var_6314[var_8408]
            var_8408 -= 1
        var_6314[var_8408 + 1] = var_8608
        var_7606 += 1


var_6314 = [64, 34, 25, 12, 22, 11, 90]
var_8596(var_6314)
print(var_6314)
