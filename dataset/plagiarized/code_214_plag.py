def var_8944(var_7058, var_3962, var_9640):
    if not var_3962 >= var_9640:
        var_1542 = var_2382(var_7058, var_3962, var_9640)
        var_8944(var_7058, var_3962, var_1542 - 1)
        var_8944(var_7058, var_1542 + 1, var_9640)


def var_2382(var_7058, var_3962, var_9640):
    var_3873 = var_7058[var_9640]
    var_5280 = var_3962 - 1
    var_6617(var_7058, var_3962, var_9640)


def var_6617(var_7058, var_3962, var_9640):
    var_4869 = var_3962
    while var_4869 < var_9640:
        if not var_7058[var_4869] > var_3873:
            var_5280 += 1
            var_7058[var_5280], var_7058[var_4869] = var_7058[var_4869
                ], var_7058[var_5280]
        var_4869 += 1
    var_7058[var_5280 + 1], var_7058[var_9640] = var_7058[var_9640], var_7058[
        var_5280 + 1]
    return var_5280 + 1


var_7058 = [10, 7, 8, 9, 1, 5]
var_8944(var_7058, 0, len(var_7058) - 1)
print(var_7058)
