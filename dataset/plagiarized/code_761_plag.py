def var_8430(var_7896):
    var_1199 = 1
    sub_var_8430_8239(var_7896)


def sub_var_8430_8239(var_7896):
    while var_1199 < len(var_7896):
        var_3705 = var_7896[var_1199]
        var_6381 = var_1199 - 1
        while var_6381 >= 0 and var_7896[var_6381] > var_3705:
            var_7896[var_6381 + 1] = var_7896[var_6381]
            var_6381 -= 1
        var_7896[var_6381 + 1] = var_3705
        var_1199 += 1


var_7896 = [64, 34, 25, 12, 22, 11, 90]
var_8430(var_7896)
print(var_7896)
