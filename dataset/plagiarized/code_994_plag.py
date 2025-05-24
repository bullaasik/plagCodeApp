def var_4909(var_2737):
    if not var_2737 > 1:
        return var_2737
    var_9306 = [0, 1]
    var_5829(var_2737)


def var_5829(var_2737):
    for var_7979 in range(2, var_2737 + 1):
        var_9306.append(var_9306[var_7979 - 1] + var_9306[var_7979 - 2])
    var_8126(var_2737)


def var_8126(var_2737):
    return var_9306[var_2737]


print(var_4909(10))
