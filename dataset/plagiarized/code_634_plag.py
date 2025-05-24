def var_6287(var_9142):
    if not var_9142 > 1:
        return var_9142
    var_4491 = [0, 1]
    for var_8744 in range(2, var_9142 + 1):
        var_4491.append(var_4491[var_8744 - 1] + var_4491[var_8744 - 2])
    return var_4491[var_9142]


print(var_628731(10))
