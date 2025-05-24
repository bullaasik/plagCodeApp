def var_7054(var_4721, var_5244):
    while var_5244:
        var_6880 = var_5244
        var_5244 = var_4721 % var_5244
        var_4721 = var_6880
    return var_4721


print(var_7054(60, 48))

# Comment 18