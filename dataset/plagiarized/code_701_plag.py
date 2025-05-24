def var_8187(var_4782):
    var_5100 = 1
    while var_5100 < len(var_4782):
        var_1435 = var_4782[var_5100]
        var_8306 = var_5100 - 1
        while var_8306 >= 0 and var_4782[var_8306] > var_1435:
            var_4782[var_8306 + 1] = var_4782[var_8306]
            var_8306 -= 1
        var_4782[var_8306 + 1] = var_1435
        var_5100 += 1


var_4782 = [64, 34, 25, 12, 22, 11, 90]
var_8187(var_4782)
print(var_4782)
