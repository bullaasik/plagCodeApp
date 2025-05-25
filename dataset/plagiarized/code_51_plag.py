def var_8213(var_1606, var_2644, var_2633):
    if not var_2644 >= var_2633:
        var_9617 = var_8486(var_1606, var_2644, var_2633)
        var_8213(var_1606, var_2644, var_9617 - 1)
        var_8213(var_1606, var_9617 + 1, var_2633)


def var_8486(var_1606, var_2644, var_2633):
    var_3068 = var_1606[var_2633]
    var_9229 = var_2644 - 1
    var_6439 = var_2644
    while var_6439 < var_2633:
        if not var_1606[var_6439] > var_3068:
            var_9229 += 1
            var_1606[var_9229], var_1606[var_6439] = var_1606[var_6439
                ], var_1606[var_9229]
        var_6439 += 1
    var_1606[var_9229 + 1], var_1606[var_2633] = var_1606[var_2633], var_1606[
        var_9229 + 1]
    return var_9229 + 1


var_1606 = [10, 7, 8, 9, 1, 5]
var_8213(var_1606, 0, len(var_1606) - 1)
print(var_1606)

# Comment 84