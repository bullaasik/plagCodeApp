def var_2665(var_9024, var_2910, var_6978):
    if not var_2910 >= var_6978:
        var_6314 = var_7683(var_9024, var_2910, var_6978)
        var_2665(var_9024, var_2910, var_6314 - 1)
        var_2665(var_9024, var_6314 + 1, var_6978)


def var_7683(var_9024, var_2910, var_6978):
    var_8955 = var_9024[var_6978]
    var_2600 = var_2910 - 1
    var_2113 = var_2910
    while var_2113 < var_6978:
        if not var_9024[var_2113] > var_8955:
            var_2600 += 1
            var_9024[var_2600], var_9024[var_2113] = var_9024[var_2113
                ], var_9024[var_2600]
        var_2113 += 1
    var_9024[var_2600 + 1], var_9024[var_6978] = var_9024[var_6978], var_9024[
        var_2600 + 1]
    return var_2600 + 1


var_9024 = [10, 7, 8, 9, 1, 5]
var_2665(var_9024, 0, len(var_9024) - 1)
print(var_9024)
