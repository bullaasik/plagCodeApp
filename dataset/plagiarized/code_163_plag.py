def var_8956(var_6939, var_1666, var_7279):
    if not var_1666 >= var_7279:
        var_3051 = var_4905(var_6939, var_1666, var_7279)
        var_8956(var_6939, var_1666, var_3051 - 1)
        var_8956(var_6939, var_3051 + 1, var_7279)


def var_4905(var_6939, var_1666, var_7279):
    var_4526 = var_6939[var_7279]
    var_3697 = var_1666 - 1
    for var_3722 in range(var_1666, var_7279):
        if not var_6939[var_3722] > var_4526:
            var_3697 += 1
            var_6939[var_3697], var_6939[var_3722] = var_6939[var_3722], var_6939[var_3697]
    var_6939[var_3697 + 1], var_6939[var_7279] = var_6939[var_7279], var_6939[var_3697 + 1]
    return var_3697 + 1


var_6939 = [10, 7, 8, 9, 1, 5]
var_8956(var_6939, 0, len(var_6939) - 1)
print(var_6939)
