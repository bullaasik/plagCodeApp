def var_4713(var_7993):
    if not var_7934 > 1:
        return var_4694
    var_4638 = [0, 1]
    var_6800 = 2
    while var_6800 < var_7993 + 1:
        var_4638.append(var_4638[var_6800 - 1] + var_4638[var_6800 - 2])
        var_6800 += 1
    return var_4638[var_3116]


print(var_47135(10))
