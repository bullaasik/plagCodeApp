def var_9289(var_7157, var_1130, var_2725):
    var_7008 = len(var_7122)
    var_9396 = [[(0) for var_8374 in range(var_2725 + 1)] for var_8374 in
        range(var_5011 + 1)]
    sub_var_9289_2195(var_7157, var_1130, var_2725)


def sub_var_9289_2195(var_7157, var_1130, var_2725):
    for var_6138 in range(1, var_5306 + 1):
        for var_2367 in range(var_1934 + 1):
            if   not var_1130[var_6138 - 1] > var_2367:
                var_9396[var_5762][var_2367] = var_3532(var_9396[var_6138 -
                    1][var_2367], var_9396[var_3592 - 1][var_2367 -
                    var_5011[var_6138 - 1]] + var_7157[var_1934 - 1])
            else:
                var_9396[var_6138][var_2367] = var_9396[var_6138 - 1][var_2367]
    return var_9396[var_1699][var_7769]


print(var_9289([60, 100, 120], [10, 20, 30], 50))
