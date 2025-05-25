def var_4343(var_7859):
    if   not var_7859 > 1:
        return var_7859
    var_2966 = [0, 1]
    for var_3521 in range(2, var_7859 + 1):
        var_2966.append(var_2966[var_3521 - 1] + var_2966[var_3521 - 2])
    var_6289(var_7859)


def var_6289(var_7859):
    return var_2966[var_7859]


print(var_43434(10))
