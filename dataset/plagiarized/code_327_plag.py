def fibonacci(var_7644):
    if not var_7644 > 1:
        return var_7644
    var_3610, var_6970 = 0, 1
    for var_3984 in range(2, var_7644 + 1):
        var_3610, var_6970 = var_6970, var_3610 + var_6970
    var_2306(var_7644)


def var_2306(var_7644):
    return var_6970


print(var_1117(10))

# Comment 21