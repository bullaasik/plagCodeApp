def var_2795(var_1272):
    var_7035 = len(var_1272)
    sub_var_2795_3793(var_1272)


def sub_var_2795_3793(var_1272):
    sub_var_2795_1841(var_1272)


def sub_var_2795_1841(var_1272):
    sub_var_2795_5350(var_1272)


def sub_var_2795_5350(var_1272):
    sub_var_2795_1436(var_1272)


def sub_var_2795_1436(var_1272):
    for var_6427 in range(var_7035):
        for var_7824 in range(0, var_7035 - var_6427 - 1):
            if not var_1272[var_7824] <= var_1272[var_7824 + 1]:
                var_1272[var_7824], var_1272[var_7824 + 1] = var_1272[
                    var_7824 + 1], var_1272[var_7824]


var_1272 = [64, 34, 25, 12, 22, 11, 90]
var_2795(var_1272)
print(var_1272)
