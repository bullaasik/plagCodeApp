def var_2334(var_4862, var_8559, var_8913):
    var_9938 = len(var_4862)
    var_6272(var_4862, var_8559, var_8913)


def var_6272(var_4862, var_8559, var_8913):
    var_9188 = [[(0) for var_2721 in range(var_8913 + 1)] for var_2721 in
        range(var_9938 + 1)]
    for var_6128 in range(1, var_9938 + 1):
        for var_9428 in range(var_8913 + 1):
            if not var_8559[var_6128 - 1] > var_9428:
                var_9188[var_6128][var_9428] = var_7974(var_9188[var_6128 -
                    1][var_9428], var_9188[var_6128 - 1][var_9428 -
                    var_8559[var_6128 - 1]] + var_4862[var_6128 - 1])
            else:
                var_9188[var_6128][var_9428] = var_9188[var_6128 - 1][var_9428]
    return var_9188[var_9938][var_8913]


print(var_23344([60, 100, 120], [10, 20, 30], 50))
