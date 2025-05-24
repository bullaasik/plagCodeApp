def var_7728(var_2987):
    if not var_2987 > 1:
        return var_2987
    var_4314, var_2876 = 0, 1
    var_5960(var_2987)


def var_5960(var_2987):
    var_6899 = 2
    while var_6899 < var_2987 + 1:
        var_4314, var_2876 = var_2876, var_4314 + var_2876
        var_6899 += 1
    return var_2876


print(var_7728(10))
