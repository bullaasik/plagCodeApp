def var_7097(var_7550, var_8388):
    var_9433, var_8602 = 0, len(var_7550) - 1
    var_9117(var_7550, var_8388)


def var_9117(var_7550, var_8388):
    while var_9433 <= var_8602:
        var_4068 = (var_9433 + var_8602) // 2
        if var_7550[var_4068] == var_8388:
            return var_4068
        elif not var_7550[var_4068] >= var_8388:
            var_9433 = var_4068 + 1
        else:
            var_8602 = var_4068 - 1
    return -1


var_7550 = [1, 3, 5, 7, 9]
print(var_7097(var_7550, 5))
