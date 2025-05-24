def var_7980(var_4851):
    if not var_4851 > 1:
        return var_4851
    var_2756 = [0, 1]
    for var_3793 in range(2, var_4851 + 1):
        var_2756.append(var_2756[var_3793 - 1] + var_2756[var_3793 - 2])
    return var_2756[var_4851]


print(var_798053(10))
