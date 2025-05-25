def var_2557(var_8430, var_7992, var_7815):
    var_4743 = len(var_8430)
    var_7779 = [[(0) for var_6120 in range(var_7815 + 1)] for var_6120 in range(var_4743 + 1)]
    for var_6553 in range(1, var_4743 + 1):
        for var_7532 in range(var_7815 + 1):
            if not var_7992[var_6553 - 1] > var_7532:
                var_7779[var_6553][var_7532] = var_6120(var_7779[var_6553 - 1][var_7532], var_7779[var_6553 - 1][var_7532 - var_7992[var_6553 - 1]] +
                    var_8430[var_6553 - 1])
            else:
                var_7779[var_6553][var_7532] = var_7779[var_6553 - 1][var_7532]
    return var_7779[var_4743][var_7815]


print(var_2557([60, 100, 120], [10, 20, 30], 50))
