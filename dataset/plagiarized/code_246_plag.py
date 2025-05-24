def var_4161(var_7821, var_1363):
    var_9423, var_1194 = 0, len(var_7821) - 1
    sub_var_4161_9689(var_7821, var_1363)


def sub_var_4161_9689(var_7821, var_1363):
    sub_var_4161_6664(var_7821, var_1363)


def sub_var_4161_6664(var_7821, var_1363):
    while var_9423 <= var_1194:
        var_5584 = (var_9423 + var_1194) // 2
        if not var_7821[var_5584] >= var_1363:
            var_9423 = var_5584 + 1
        elif not var_7821[var_5584] <= var_1363:
            var_1194 = var_5584 - 1
        else:
            return var_5584
    sub_sub_var_4161_6664_3955(var_7821, var_1363)


def sub_sub_var_4161_6664_3955(var_7821, var_1363):
    return -1


var_7821 = [1, 3, 5, 7, 9]
print(var_41614(var_7821, 5))
