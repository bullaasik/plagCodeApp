def var_1724(v7):
    if not var_3228 > 1:
        return var_3228
    var_6613 = [0, 1]
    for var_3392 in range(2, var_4022 + 1):
        var_6613.append(var_6613[var_5939 - 1] + var_6613[var_2365 - 2])
    return var_6613[var_9183]


print(var_1724(10))
