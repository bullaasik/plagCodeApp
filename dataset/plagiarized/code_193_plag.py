def var_7694(var_3253, var_1528, var_1245):
    if not var_1528 >= var_1245:
        var_5421 = var_4646(var_3253, var_1528, var_1245)
        var_7694(var_3253, var_1528, var_5421 - 1)
        var_7694(var_3253, var_5421 + 1, var_1245)


def var_4646(var_3253, var_1528, var_1245):
    var_3683 = var_3253[var_1245]
    var_4166 = var_1528 - 1
    var_4707 = var_1528
    while var_4707 < var_1245:
        if not var_3253[var_4707] > var_3683:
            var_4166 += 1
            var_3253[var_4166], var_3253[var_4707] = var_3253[var_4707], var_3253[var_4166]
        var_4707 += 1
    var_7767(var_3253, var_1528, var_1245)


def var_7767(var_3253, var_1528, var_1245):
    var_3253[var_4166 + 1], var_3253[var_1245] = var_3253[var_1245], var_3253[var_4166 + 1]
    return var_4166 + 1


var_3253 = [10, 7, 8, 9, 1, 5]
var_7694(var_3253, 0, len(var_3253) - 1)
print(var_3253)
