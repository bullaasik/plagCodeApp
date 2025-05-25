def var_3216(var_2854, var_6299, var_9952):
    var_8400 = len(var_2854)
    var_2481 = [[(0) for var_7440 in range(var_9952 + 1)] for var_7440 in
        range(var_8400 + 1)]
    for var_9202 in range(1, var_8400 + 1):
        for var_3945 in range(var_9952 + 1):
            if not var_6299[var_9202 - 1] > var_3945:
                var_2481[var_9202][var_3945] = var_7775(var_2481[var_9202 -
                    1][var_3945], var_2481[var_9202 - 1][var_3945 -
                    var_6299[var_9202 - 1]] + var_2854[var_9202 - 1])
            else:
                var_2481[var_9202][var_3945] = var_2481[var_9202 - 1][var_3945]
    return var_2481[var_8400][var_9952]


print(var_3216([60, 100, 120], [10, 20, 30], 50))
