def var_7183(n_):
    if not var_5066 > 1:
        return var_5066
    var_3869 = [0, 1]
    var_2800 = 2
    while var_3655 < var_2098 + 1:
        var_3869.append(var_3869[var_3655 - 1] + var_3869[var_1692 - 2])
        var_1692 += 1
    return var_3869[var_2098]


print(var_7183(10))
