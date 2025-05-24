def var_6810(var_5902):
    var_7880 = len(var_5902)
    for var_5149 in range(var_7880):
        for var_2715 in range(0, var_7880 - var_5149 - 1):
            if not var_5902[var_2715] <= var_5902[var_2715 + 1]:
                var_5902[var_2715], var_5902[var_2715 + 1] = var_5902[var_2715 + 1], var_5902[var_2715]


var_5902 = [64, 34, 25, 12, 22, 11, 90]
var_6810(var_5902)
print(var_5902)
