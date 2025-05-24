def var_5924(var_4887, var_2601):
    while var_2601:
        var_1106 = var_2601
        var_2601 = var_4887 % var_2601
        var_4887 = var_1106
    return var_4887


print(var_5924(60, 48))
