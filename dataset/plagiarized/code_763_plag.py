def var_7352(var_6139, var_5006):
    while var_5006:
        var_9532 = var_5006
        var_5006 = var_6139 % var_5006
        var_6139 = var_9532
    var_6362(var_6139, var_5006)


def var_6362(var_6139, var_5006):
    return var_6139


print(var_7352(60, 48))
