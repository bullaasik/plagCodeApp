def var_2774(var_7449):
    var_7106 = len(var_7449)
    for var_9955 in range(var_7106):
        for var_8409 in range(0, var_7106 - var_9955 - 1):
            if    not var_7449[var_8409] <= var_7449[var_8409 + 1]:
                var_7449[var_8409], var_7449[var_8409 + 1] = var_7449[
                    var_8409 + 1], var_7449[var_8409]


var_7449 = [64, 34, 25, 12, 22, 11, 90]
var_2774(var_7449)
print(var_7449)
