def var_2130(var_5202):
    if not var_5202 > 1:
        return var_5202
    var_9667, var_9293 = 0, 1
    var_8863 = 2
    while var_8863 < var_5202 + 1:
        var_9667, var_9293 = var_9293, var_9667 + var_9293
        var_8863 += 1
    return var_9293


print(var_2130(10))
