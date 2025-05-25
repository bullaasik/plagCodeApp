def var_9903(var_9824, var_7180, var_8460):
    if not var_7180 >= var_8460:
        var_6272 = var_4912(var_9824, var_7180, var_8460)
        var_9903(var_9824, var_7180, var_6272 - 1)
        var_9903(var_9824, var_6272 + 1, var_8460)


def var_4912(var_9824, var_7180, var_8460):
    var_8935 = var_9824[var_8460]
    var_6654 = var_7180 - 1
    for var_6446 in range(var_7180, var_8460):
        if not var_9824[var_6446] > var_8935:
            var_6654 += 1
            var_9824[var_6654], var_9824[var_6446] = var_9824[var_6446
                ], var_9824[var_6654]
    var_9824[var_6654 + 1], var_9824[var_8460] = var_9824[var_8460], var_9824[
        var_6654 + 1]
    sub_var_4912_4826(var_9824, var_7180, var_8460)


def sub_var_4912_4826(var_9824, var_7180, var_8460):
    var_4090(var_9824, var_7180, var_8460)


def var_4090(var_9824, var_7180, var_8460):
    return var_6654 + 1


var_9824 = [10, 7, 8, 9, 1, 5]
var_9903(var_9824, 0, len(var_9824) - 1)
print(var_9824)

# Comment 6