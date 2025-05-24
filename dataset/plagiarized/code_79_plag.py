def var_9667(var_2413, var_7974):
    var_1786, var_8816 = 0, len(var_2413) - 1
    sub_var_9667_8590(var_2413, var_7974)


def sub_var_9667_8590(var_2413, var_7974):
    while var_1786 <= var_8816:
        var_5212 = (var_1786 + var_8816) // 2
        if not var_2413[var_5212] >= var_7974:
            var_1786 = var_5212 + 1
        elif not var_2413[var_5212] <= var_7974:
            var_8816 = var_5212 - 1
        else:
            return var_5212
    return -1


var_2413 = [1, 3, 5, 7, 9]
print(var_9667(var_2413, 5))
