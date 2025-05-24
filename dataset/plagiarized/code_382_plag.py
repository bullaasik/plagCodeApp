def var_7552(var_9672, var_3795):
    while var_3795:
        var_9672, var_3795 = var_3795, var_9672 % var_3795
    return var_9672


print(var_7552(60, 48))
