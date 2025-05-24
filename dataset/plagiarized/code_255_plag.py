def var_5650(var_1047):
    var_5187 = len(var_1047)
    sub_var_5650_4788(var_1047)


def sub_var_5650_4788(var_1047):
    for var_6805 in range(var_5187):
        for var_4430 in range(0, var_5187 - var_6805 - 1):
            if not var_1047[var_4430] <= var_1047[var_4430 + 1]:
                var_1047[var_4430], var_1047[var_4430 + 1] = var_1047[
                    var_4430 + 1], var_1047[var_4430]


var_1047 = [64, 34, 25, 12, 22, 11, 90]
var_5650(var_1047)
print(var_1047)
