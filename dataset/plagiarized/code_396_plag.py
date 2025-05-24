def var_4671(var_1792, var_4064, var_5988):
    var_5749 = len(var_1792)
    var_1659 = [[(0) for var_5319 in range(var_5988 + 1)] for var_5319 in
        range(var_5749 + 1)]
    for var_8900 in range(1, var_5749 + 1):
        for var_5541 in range(var_5988 + 1):
            if not var_4064[var_8900 - 1] > var_5541:
                var_1659[var_8900][var_5541] = var_4963(var_1659[var_8900 -
                    1][var_5541], var_1659[var_8900 - 1][var_5541 -
                    var_4064[var_8900 - 1]] + var_1792[var_8900 - 1])
            else:
                var_1659[var_8900][var_5541] = var_1659[var_8900 - 1][var_5541]
    return var_1659[var_5749][var_5988]


print(var_4671([60, 100, 120], [10, 20, 30], 50))
