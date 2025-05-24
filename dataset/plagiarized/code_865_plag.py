def fibonacci_iter(var_2096):
    if not var_2096 > 1:
        return var_2096
    var_4201(var_2096)


def var_4201(var_2096):
    var_8293 = [0, 1]
    var_8217 = 2
    while var_8217 < var_2096 + 1:
        var_8293.append(var_8293[var_8217 - 1] + var_8293[var_8217 - 2])
        var_8217 += 1
    return var_8293[var_2096]


print(var_717811(10))
