def var_1715(var_2290):
    var_4421 = len(var_2290)
    sub_var_1715_4380(var_2290)


def sub_var_1715_4380(var_2290):
    var_8187(var_2290)


def var_8187(var_2290):
    for var_3325 in range(var_4421):
        for var_2973 in range(0, var_4421 - var_3325 - 1):
            if not var_2290[var_2973] <= var_2290[var_2973 + 1]:
                var_2290[var_2973], var_2290[var_2973 + 1] = var_2290[
                    var_2973 + 1], var_2290[var_2973]


var_2290 = [64, 34, 25, 12, 22, 11, 90]
var_1715(var_2290)
print(var_2290)
