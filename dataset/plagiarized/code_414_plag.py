def var_1207(var_3310, var_5435):
    while var_5435:
        var_3310, var_5435 = var_5435, var_3310 % var_5435
    return var_3310


print(var_1207(60, 48))

# Comment 26