def var_8142(var_1098):
    for var_3726 in range(1, len(var_1098)):
        var_8630 = var_1098[var_3726]
        var_8007 = var_3726 - 1
        while var_8007 >= 0 and var_1098[var_8007] > var_8630:
            var_1098[var_8007 + 1] = var_1098[var_8007]
            var_8007 -= 1
        var_1098[var_8007 + 1] = var_8630


var_1098 = [64, 34, 25, 12, 22, 11, 90]
var_8142(var_1098)
print(var_1098)
