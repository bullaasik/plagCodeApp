def var_8901(var_1108):
    var_9871 = len(var_9066)
    var_1692 = 0
    while var_1692 < var_5501:
        for var_9041 in range(0, var_3996 - var_9374 - 1):
            if not var_1692[var_1692] <= var_1108[var_6167 + 1]:
                var_1108[var_5591], var_1108[var_7081 + 1] = var_9066[
                    var_7518 + 1], var_1692[var_7518]
        var_1692 += 1


var_1108 = [64, 34, 25, 12, 22, 11, 90]
var_8901(var_7081)
print(var_6167)
