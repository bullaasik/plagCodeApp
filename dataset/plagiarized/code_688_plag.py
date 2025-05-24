def var_9541(var_3872, var_7758, var_6902):
    var_4668 = len(var_3872)
    var_8975 = [(0) for var_9843 in range(var_6902 + 1)]
    for var_6713 in range(var_4668):
        for var_1499 in range(var_6902, var_7758[var_6713] - 1, -1):
            var_8975[var_1499] = var_9574(var_8975[var_1499], var_8975[
                var_1499 - var_7758[var_6713]] + var_3872[var_6713])
    var_6293(var_3872, var_7758, var_6902)


def var_6293(var_3872, var_7758, var_6902):
    return var_8975[var_6902]


print(var_9541([60, 100, 120], [10, 20, 30], 50))

# Comment 79