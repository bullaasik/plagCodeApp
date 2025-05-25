def var_7043(var_8619):
    if not var_8619 > 1:
        return var_8619
    sub_var_7043_3683(var_8619)


def sub_var_7043_3683(var_8619):
    var_5198, var_4571 = 0, 1
    var_2874 = 2
    while var_2874 < var_8619 + 1:
        var_5198, var_4571 = var_4571, var_5198 + var_4571
        var_2874 += 1
    return var_4571


print(var_7043(10))
