def var_5124(var_4191):
    var_8475 = len(var_4191)
    sub_var_5124_9070(var_4191)


def sub_var_5124_9070(var_4191):
    var_1008 = 0
    while var_1008 < var_8475:
        for var_7671 in range(0, var_8475 - var_1008 - 1):
            if not var_4191[var_7671] <= var_4191[var_7671 + 1]:
                var_4191[var_7671], var_4191[var_7671 + 1] = var_4191[
                    var_7671 + 1], var_4191[var_7671]
        var_1008 += 1


var_4191 = [64, 34, 25, 12, 22, 11, 90]
var_5124(var_4191)
print(var_4191)
