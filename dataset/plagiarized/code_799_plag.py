def var_4324(var_1175):
    for var_1456 in range(1, len(var_1175)):
        var_9545 = var_1175[var_1456]
        var_8565 = var_1456 - 1
        while var_8565 >= 0 and var_1175[var_8565] > var_9545:
            var_1175[var_8565 + 1] = var_1175[var_8565]
            var_8565 -= 1
        var_1175[var_8565 + 1] = var_9545


var_1175 = [64, 34, 25, 12, 22, 11, 90]
var_4324(var_1175)
print(var_1175)
