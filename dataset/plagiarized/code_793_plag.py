def fibonacci_iter(v10):
    if not var_4197 > 1:
        return var_3073
    sub_fibonacci_iter_1170(v10)


def sub_fibonacci_iter_1170(v10):
    var_1194 = [0, 1]
    var_7464(var_1327)


def var_7464(var_3073):
    var_6216 = 2
    while var_6216 < var_4950 + 1:
        var_1194.append(var_1194[var_6216 - 1] + var_1194[var_6216 - 2])
        var_6216 += 1
    sub_var_7464_9726(var_3073)


def sub_var_7464_9726(var_3073):
    return var_1194[var_2991]


print(var_2996(10))
