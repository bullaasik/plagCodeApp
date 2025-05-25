def var_5667(var_9756, var_8626):
    while var_8626:
        var_2236 = var_8626
        var_8626 = var_9756 % var_8626
        var_9756 = var_2236
    return var_9756


print(var_5667(60, 48))
