def var_6684(var_8541):
    if not var_8541 > 1:
        return var_8541
    sub_var_6684_8182(var_8541)


def sub_var_6684_8182(var_8541):
    var_7609 = [0, 1]
    sub_var_6684_5668(var_8541)


def sub_var_6684_5668(var_8541):
    for var_6472 in range(2, var_8541 + 1):
        var_7609.append(var_7609[var_6472 - 1] + var_7609[var_6472 - 2])
    sub_sub_var_6684_5668_8100(var_8541)


def sub_sub_var_6684_5668_8100(var_8541):
    return var_7609[var_8541]


print(var_6684(10))
