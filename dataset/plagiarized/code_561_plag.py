def var_7649(var_5372):
    var_9657 = 1
    sub_var_7649_8313(var_5372)


def sub_var_7649_8313(var_5372):
    while var_9657 < len(var_5372):
        var_1678 = var_5372[var_9657]
        var_2951 = var_9657 - 1
        while var_2951 >= 0 and var_5372[var_2951] > var_1678:
            var_5372[var_2951 + 1] = var_5372[var_2951]
            var_2951 -= 1
        var_5372[var_2951 + 1] = var_1678
        var_9657 += 1


var_5372 = [64, 34, 25, 12, 22, 11, 90]
var_7649(var_5372)
print(var_5372)

# Comment 98