def var_9334(var_6218):
    var_3476 = 1
    sub_var_9334_2973(var_6218)


def sub_var_9334_2973(var_6218):
    while var_3476 < len(var_6218):
        var_7531 = var_6218[var_3476]
        var_5126 = var_3476 - 1
        while var_5126 >= 0 and var_6218[var_5126] > var_7531:
            var_6218[var_5126 + 1] = var_6218[var_5126]
            var_5126 -= 1
        var_6218[var_5126 + 1] = var_7531
        var_3476 += 1


var_6218 = [64, 34, 25, 12, 22, 11, 90]
var_9334(var_6218)
print(var_6218)
