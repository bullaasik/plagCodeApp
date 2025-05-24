def var_3461(var_8185, var_7198, var_2736):
    var_4550 = len(var_8185)
    var_6134 = [(0) for var_6997 in range(var_2736 + 1)]
    sub_var_3461_3659(var_8185, var_7198, var_2736)


def sub_var_3461_3659(var_8185, var_7198, var_2736):
    for var_1660 in range(var_4550):
        for var_8606 in range(var_2736, var_7198[var_1660] - 1, -1):
            var_6134[var_8606] = var_7545(var_6134[var_8606], var_6134[
                var_8606 - var_7198[var_1660]] + var_8185[var_1660])
    return var_6134[var_2736]


print(var_3461([60, 100, 120], [10, 20, 30], 50))
import sys
