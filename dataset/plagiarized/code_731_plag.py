def var_8522(var_2501, var_7506):
    while var_7506:
        var_1802 = var_7506
        var_7506 = var_2501 % var_7506
        var_2501 = var_1802
    return var_2501


print(var_8522(60, 48))

# Comment 78