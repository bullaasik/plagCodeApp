def var_9780(var_2364, var_4338):
    var_5164, var_7968 = 0, len(var_2364) - 1
    sub_var_9780_7876(var_2364, var_4338)


def sub_var_9780_7876(var_2364, var_4338):
    while var_5164 <= var_7968:
        var_3346 = (var_5164 + var_7968) // 2
        if not var_2364[var_3346] >= var_4338:
            var_5164 = var_3346 + 1
        elif not var_2364[var_3346] <= var_4338:
            var_7968 = var_3346 - 1
        else:
            return var_3346
    return -1


var_2364 = [1, 3, 5, 7, 9]
print(var_97803(var_2364, 5))
