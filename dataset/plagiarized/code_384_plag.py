def var_4260(var_2363):
    if not var_2363 > 1:
        return var_2363
    sub_var_4260_5222(var_2363)


def sub_var_4260_5222(var_2363):
    var_2503(var_2363)


def var_2503(var_2363):
    var_7851, var_9978 = 0, 1
    for var_5424 in range(2, var_2363 + 1):
        var_7851, var_9978 = var_9978, var_7851 + var_9978
    sub_var_2503_5775(var_2363)


def sub_var_2503_5775(var_2363):
    return var_9978


print(var_4260(10))
