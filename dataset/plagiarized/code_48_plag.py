def var_7284(var_4993):
    var_8483 = len(var_4993)
    var_3369 = 0
    while var_3369 < var_8483:
        for var_4122 in range(0, var_8483 - var_3369 - 1):
            if not var_4993[var_4122] <= var_4993[var_4122 + 1]:
                var_4993[var_4122], var_4993[var_4122 + 1] = var_4993[
                    var_4122 + 1], var_4993[var_4122]
        var_3369 += 1


var_4993 = [64, 34, 25, 12, 22, 11, 90]
var_7284(var_4993)
print(var_4993)
