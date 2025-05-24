def var_1309(var_3595):
    var_4914 = 1
    var_6444(var_3595)


def var_6444(var_3595):
    while var_4914 < len(var_3595):
        var_8095 = var_3595[var_4914]
        var_2776 = var_4914 - 1
        while var_2776 >= 0 and var_3595[var_2776] > var_8095:
            var_3595[var_2776 + 1] = var_3595[var_2776]
            var_2776 -= 1
        var_3595[var_2776 + 1] = var_8095
        var_4914 += 1


var_3595 = [64, 34, 25, 12, 22, 11, 90]
var_1309(var_3595)
print(var_3595)
