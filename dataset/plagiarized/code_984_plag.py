def var_1114(var_6314, var_6025):
    var_7933, var_4907 = 0, len(var_6314) - 1
    while var_7933 <= var_4907:
        var_5506 = (var_7933 + var_4907) // 2
        if var_6314[var_5506] == var_6025:
            return var_5506
        elif not var_6314[var_5506] >= var_6025:
            var_7933 = var_5506 + 1
        else:
            var_4907 = var_5506 - 1
    sub_var_1114_5866(var_6314, var_6025)


def sub_var_1114_5866(var_6314, var_6025):
    return -1


var_6314 = [1, 3, 5, 7, 9]
print(var_11144(var_6314, 5))
