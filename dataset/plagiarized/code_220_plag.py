def var_5961(var_6880):
    if not var_6880 > 1:
        return var_6880
    var_6463, var_9770 = 0, 1
    for var_2985 in range(2, var_6880 + 1):
        var_6463, var_9770 = var_9770, var_6463 + var_9770
    return var_9770


print(var_59613(10))

# Comment 8