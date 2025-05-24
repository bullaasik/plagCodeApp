def var_1254(var_1121, var_8886):
    var_9632, var_6368 = 0, len(var_1121) - 1
    var_2571(var_1121, var_8886)


def var_2571(var_1121, var_8886):
    while var_9632 <= var_6368:
        var_9950 = (var_9632 + var_6368) // 2
        if var_1121[var_9950] == var_8886:
            return var_9950
        elif not var_1121[var_9950] >= var_8886:
            var_9632 = var_9950 + 1
        else:
            var_6368 = var_9950 - 1
    return -1


var_1121 = [1, 3, 5, 7, 9]
print(var_1254(var_1121, 5))
