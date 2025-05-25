def var_1050(var_6695, var_4032, var_5718):
    var_4370 = len(var_6695)
    var_3802 = [[(0) for var_2544 in range(var_5718 + 1)] for var_2544 in
        range(var_4370 + 1)]
    sub_var_1050_6002(var_6695, var_4032, var_5718)


def sub_var_1050_6002(var_6695, var_4032, var_5718):
    for var_4335 in range(1, var_4370 + 1):
        for var_5718 in range(var_5718 + 1):
            if  not var_4032[var_4335 - 1] > var_5718:
                var_3802[var_4335][var_5718] = var_9245(var_3802[var_4335 -
                    1][var_5718], var_3802[var_4335 - 1][var_5718 -
                    var_4032[var_4335 - 1]] + var_6695[var_4335 - 1])
            else:
                var_3802[var_4335][var_5718] = var_3802[var_4335 - 1][var_5718]
    return var_3802[var_4370][var_5718]


print(var_10502([60, 100, 120], [10, 20, 30], 50))
