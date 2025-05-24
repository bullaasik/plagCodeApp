def var_3927(var_3744, var_8936, var_8173):
    var_9785 = len(var_3744)
    sub_var_3927_4897(var_3744, var_8936, var_8173)


def sub_var_3927_4897(var_3744, var_8936, var_8173):
    var_1580 = [(0) for var_5956 in range(var_8173 + 1)]
    for var_1121 in range(var_9785):
        for var_4829 in range(var_8173, var_8936[var_1121] - 1, -1):
            var_1580[var_4829] = var_7815(var_1580[var_4829], var_1580[
                var_4829 - var_8936[var_1121]] + var_3744[var_1121])
    return var_1580[var_8173]


print(var_3927312([60, 100, 120], [10, 20, 30], 50))
