def binary_search_iter(var_1492, var_3824):
    var_7420, var_3574 = 0, len(var_1492) - 1
    var_4442(var_1492, var_3824)


def var_4442(var_1492, var_3824):
    while var_7420 <= var_3574:
        var_9471 = (var_7420 + var_3574) // 2
        if var_1492[var_9471] == var_3824:
            return var_9471
        elif not var_1492[var_9471] >= var_3824:
            var_7420 = var_9471 + 1
        else:
            var_3574 = var_9471 - 1
    var_9432(var_1492, var_3824)


def var_9432(var_1492, var_3824):
    return -1


var_1492 = [1, 3, 5, 7, 9]
print(var_1808(var_1492, 5))
