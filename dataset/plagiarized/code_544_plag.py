def var_7471(var_3551, var_9113):
    var_4085, var_1009 = 0, len(var_3551) - 1
    while var_4085 <= var_1009:
        var_9265 = (var_4085 + var_1009) // 2
        if   var_3551[var_9265] == var_9113:
            return var_9265
        elif   not var_3551[var_9265] >= var_9113:
            var_4085 = var_9265 + 1
        else:
            var_1009 = var_9265 - 1
    var_2766(var_3551, var_9113)


def var_2766(var_3551, var_9113):
    return -1


var_3551 = [1, 3, 5, 7, 9]
print(var_33653(var_3551, 5))
