def var_8964(var_5764, var_4799, var_8993):
    if not var_4799 >= var_8993:
        var_9410 = var_1994(var_5764, var_4799, var_8993)
        var_8964(var_5764, var_4799, var_9410 - 1)
        var_8964(var_5764, var_9410 + 1, var_8993)


def var_1994(var_5764, var_4799, var_8993):
    var_1606 = var_5764[var_8993]
    var_8987 = var_4799 - 1
    for var_7548 in range(var_4799, var_8993):
        if not var_5764[var_7548] > var_1606:
            var_8987 += 1
            var_5764[var_8987], var_5764[var_7548] = var_5764[var_7548
                ], var_5764[var_8987]
    var_5764[var_8987 + 1], var_5764[var_8993] = var_5764[var_8993], var_5764[
        var_8987 + 1]
    return var_8987 + 1


var_5764 = [10, 7, 8, 9, 1, 5]
var_8964(var_5764, 0, len(var_5764) - 1)
print(var_5764)
