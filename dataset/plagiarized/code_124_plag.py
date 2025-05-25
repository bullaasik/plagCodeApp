def var_5602(var_6636, var_3946, var_1427):
    if not var_3946 >= var_1427:
        var_6224 = var_4588(var_6636, var_3946, var_1427)
        var_1480(var_6636, var_3946, var_6224 - 1)
        var_5602(var_6636, var_6224 + 1, var_1427)


def var_4588(var_6636, var_3946, var_1427):
    var_9231 = var_6636[var_1427]
    var_6269 = var_3946 - 1
    for var_7363 in range(var_3946, var_1427):
        if not var_6636[var_7363] > var_9231:
            var_6269 += 1
            var_6636[var_6269], var_6636[var_7363] = var_6636[var_7363], var_6636[var_6269]
    var_6636[var_6269 + 1], var_6636[var_1427] = var_6636[var_1427], var_6636[var_6269 + 1]
    return var_6269 + 1


var_6636 = [10, 7, 8, 9, 1, 5]
var_5430(var_6636, 0, len(var_6636) - 1)
print(var_6636)
