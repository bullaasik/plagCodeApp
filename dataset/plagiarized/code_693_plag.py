def var_9496(var_4028):
    if not var_4028 > 1:
        return var_4028
    var_1700 = [0, 1]
    var_4193 = 2
    while var_4193 < var_4028 + 1:
        var_1700.append(var_1700[var_4193 - 1] + var_1700[var_4193 - 2])
        var_4193 += 1
    var_9358(var_4028)


def var_9358(var_4028):
    return var_1700[var_4028]


print(var_9496(10))
