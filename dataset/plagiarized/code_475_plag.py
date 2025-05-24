def var_2995(var_5604, var_4276):
    var_1553, var_8116 = 0, len(var_5604) - 1
    while var_1553 <= var_8116:
        var_4823 = (var_1553 + var_8116) // 2
        if not var_5604[var_4823] >= var_4276:
            var_1553 = var_4823 + 1
        elif not var_5604[var_4823] <= var_4276:
            var_8116 = var_4823 - 1
        else:
            return var_4823
    sub_var_2995_9952(var_5604, var_4276)


def sub_var_2995_9952(var_5604, var_4276):
    return -1


var_5604 = [1, 3, 5, 7, 9]
print(var_2995(var_5604, 5))
