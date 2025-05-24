def var_9203(var_3647, var_2437, var_9041):
    if not var_2437 >= var_9041:
        var_2811 = var_8183(var_3647, var_2437, var_9041)
        var_9203(var_3647, var_2437, var_2811 - 1)
        var_9203(var_3647, var_2811 + 1, var_9041)


def var_8183(var_3647, var_2437, var_9041):
    var_7607 = var_3647[var_9041]
    var_5123 = var_2437 - 1
    var_3960 = var_2437
    while var_3960 < var_9041:
        if not var_3647[var_3960] > var_7607:
            var_5123 += 1
            var_3647[var_5123], var_3647[var_3960] = var_3647[var_3960
                ], var_3647[var_5123]
        var_3960 += 1
    var_3647[var_5123 + 1], var_3647[var_9041] = var_3647[var_9041], var_3647[
        var_5123 + 1]
    return var_5123 + 1


var_3647 = [10, 7, 8, 9, 1, 5]
var_9203(var_3647, 0, len(var_3647) - 1)
print(var_3647)
