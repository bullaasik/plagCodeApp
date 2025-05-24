def var_6862(var_1164, var_5452):
    while var_5452:
        var_5589 = var_5452
        var_5452 = var_1164 % var_5452
        var_1164 = var_5589
    return var_1164


print(var_686231(60, 48))
