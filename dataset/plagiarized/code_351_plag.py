def var_2334(var_3327, var_9720, var_1777):
    if not var_9720 >= var_1777:
        var_5843 = var_2921(var_3327, var_9720, var_1777)
        var_2334(var_3327, var_9720, var_5843 - 1)
        var_2334(var_3327, var_5843 + 1, var_1777)


def var_2921(var_3327, var_9720, var_1777):
    var_1140 = var_3327[var_1777]
    var_7609 = var_9720 - 1
    for var_2044 in range(var_9720, var_1777):
        if not var_3327[var_2044] > var_1140:
            var_7609 += 1
            var_3327[var_7609], var_3327[var_2044] = var_3327[var_2044], var_3327[var_7609]
    var_3327[var_7609 + 1], var_3327[var_1777] = var_3327[var_1777], var_3327[var_7609 + 1]
    return var_7609 + 1


var_3327 = [10, 7, 8, 9, 1, 5]
var_2334(var_3327, 0, len(var_3327) - 1)
print(var_3327)

# Comment 52
# Comment 47