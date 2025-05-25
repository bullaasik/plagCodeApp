def var_5034(var_4245, var_9589, var_2173):
    if not var_9589 >= var_2173:
        var_4970 = var_5362(var_4245, var_9589, var_2173)
        var_5034(var_4245, var_9589, var_4970 - 1)
        var_5034(var_4245, var_4970 + 1, var_2173)


def var_5362(var_4245, var_9589, var_2173):
    var_8993 = var_4245[var_2173]
    var_7476 = var_9589 - 1
    var_4212 = var_9589
    while var_4212 < var_2173:
        if not var_4245[var_4212] > var_8993:
            var_7476 += 1
            var_4245[var_7476], var_4245[var_4212] = var_4245[var_4212
                ], var_4245[var_7476]
        var_4212 += 1
    var_4245[var_7476 + 1], var_4245[var_2173] = var_4245[var_2173], var_4245[
        var_7476 + 1]
    return var_7476 + 1


var_4245 = [10, 7, 8, 9, 1, 5]
var_5034(var_4245, 0, len(var_4245) - 1)
print(var_4245)

# Comment 42