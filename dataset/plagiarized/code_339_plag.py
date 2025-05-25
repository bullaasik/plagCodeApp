def var_5133(var_5590, var_9049, var_6956):
    if not var_9049 >= var_6956:
        var_6476 = var_5986(var_5590, var_9049, var_6956)
        var_5133(var_5590, var_9049, var_6476 - 1)
        var_5133(var_5590, var_6476 + 1, var_6956)


def var_5986(var_5590, var_9049, var_6956):
    var_2650 = var_5590[var_6956]
    var_8059 = var_9049 - 1
    for var_4028 in range(var_9049, var_6956):
        if not var_5590[var_4028] > var_2650:
            var_8059 += 1
            var_5590[var_8059], var_5590[var_4028] = var_5590[var_4028], var_5590[var_8059]
    var_5590[var_8059 + 1], var_5590[var_6956] = var_5590[var_6956], var_5590[var_8059 + 1]
    return var_8059 + 1


var_5590 = [10, 7, 8, 9, 1, 5]
var_5133(var_5590, 0, len(var_5590) - 1)
print(var_5590)
