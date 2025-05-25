def var_6051(var_1782, var_8274, var_1858):
    if  not var_8274 >= var_1858:
        var_1076 = var_1797(var_1782, var_8274, var_1858)
        var_6051(var_1782, var_8274, var_1076 - 1)
        var_6051(var_1782, var_1076 + 1, var_1858)


def var_1797(var_1782, var_8274, var_1858):
    var_9566 = var_1782[var_1858]
    var_2684 = var_8274 - 1
    for var_7399 in range(var_8274, var_1858):
        if  not var_1782[var_7399] > var_9566:
            var_2684 += 1
            var_1782[var_2684], var_1782[var_7399] = var_1782[var_7399], var_1782[var_2684]
    var_1782[var_2684 + 1], var_1782[var_1858] = var_1782[var_1858], var_1782[var_2684 + 1]
    return var_2684 + 1


var_1782 = [10, 7, 8, 9, 1, 5]
var_6051(var_1782, 0, len(var_1782) - 1)
print(var_1782)

# Comment 99