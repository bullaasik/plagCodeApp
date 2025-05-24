def var_7334(var_7210):
    if not var_7210 > 1:
        return var_7210
    var_4198 = [0, 1]
    var_5197 = 2
    while var_5197 < var_7210 + 1:
        var_4198.append(var_4198[var_5197 - 1] + var_4198[var_5197 - 2])
        var_5197 += 1
    return var_4198[var_7210]


print(var_7334(10))
