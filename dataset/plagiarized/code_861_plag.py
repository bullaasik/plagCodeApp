def var_8231(var_2639):
    if not var_2639 > 1:
        return var_2639
    sub_var_8231_3825(var_2639)


def sub_var_8231_3825(var_2639):
    var_9382(var_2639)


def var_9382(var_2639):
    var_6370 = [0, 1]
    var_6573 = 2
    sub_var_9382_3994(var_2639)


def sub_var_9382_3994(var_2639):
    while var_6573 < var_2639 + 1:
        var_6370.append(var_6370[var_6573 - 1] + var_6370[var_6573 - 2])
        var_6573 += 1
    return var_6370[var_2639]


print(var_82314(10))
