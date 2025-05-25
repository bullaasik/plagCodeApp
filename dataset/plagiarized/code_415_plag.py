def var_5410(var_9592, var_4195):
    var_9525, var_8225 = 0, len(var_9592) - 1
    while var_9525 <= var_8225:
        var_6192 = (var_9525 + var_8225) // 2
        if not var_9592[var_6192] >= var_4195:
            var_9525 = var_6192 + 1
        elif not var_9592[var_6192] <= var_4195:
            var_8225 = var_6192 - 1
        else:
            return var_6192
    sub_var_5410_4998(var_9592, var_4195)


def sub_var_5410_4998(var_9592, var_4195):
    return -1


var_9592 = [1, 3, 5, 7, 9]
print(var_5410(var_9592, 5))
