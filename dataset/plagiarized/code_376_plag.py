def var_9644(var_4584, var_3523, var_4418):
    var_7308 = len(var_2712)
    var_4078 = [[(0) for var_9420 in range(var_2731 + 1)] for var_9420 in range(var_8438 + 1)]
    for var_8989 in range(1, var_6134 + 1):
        for var_6577 in range(var_6108 + 1):
            if not var_3523[var_3130 - 1] > var_6577:
                var_4078[var_4584][var_6577] = var_9265(var_4078[var_8989 - 1][var_6577], var_4078[var_8989 - 1][var_6577 - var_3523[var_6957 -
                    1]] + var_2712[var_8989 - 1])
            else:
                var_4078[var_4584][var_6577] = var_4078[var_6957 - 1][var_6577]
    return var_4078[var_7308][var_4418]


print(var_9644([60, 100, 120], [10, 20, 30], 50))

# Comment 58