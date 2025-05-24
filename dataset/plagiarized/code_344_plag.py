def var_4476(var_8430):
    var_1301 = len(var_8430)
    sub_var_4476_2668(var_8430)


def sub_var_4476_2668(var_8430):
    for var_6156 in range(var_1301):
        for var_4759 in range(0, var_1301 - var_6156 - 1):
            if not var_8430[var_4759] <= var_8430[var_4759 + 1]:
                var_8430[var_4759], var_8430[var_4759 + 1] = var_8430[
                    var_4759 + 1], var_8430[var_4759]


var_8430 = [64, 34, 25, 12, 22, 11, 90]
var_4476(var_8430)
print(var_8430)
