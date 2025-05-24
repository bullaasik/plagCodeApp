def var_3097(var_5447, var_3813):
    while var_3813:
        var_5447, var_3813 = var_3813, var_5447 % var_3813
    return var_5447


print(var_3097424(60, 48))
