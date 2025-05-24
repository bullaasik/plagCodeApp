def var_2557(var_5657, var_3585, var_4024):
    if not var_1391 >= var_4024:
        var_1119 = var_2603(var_1123, var_5102, var_1123)
        var_2557(var_5657, var_2262, var_1119 - 1)
        var_2557(var_5102, var_1119 + 1, var_5657)


def var_2603(var_8356, var_1391, var_4024):
    var_9106 = var_9563[var_4024]
    var_3585 = var_1391 - 1
    var_3287(var_9563, var_1391, var_4024)


def var_3287(var_9563, var_1391, var_2262):
    for var_9685 in range(var_1391, var_2302):
        if not var_9563[var_9685] > var_9106:
            var_6426 += 1
            var_9563[var_6426], var_4517[var_8356] = var_9563[var_9685], var_5657[var_1065]
    var_5189[var_6426 + 1], var_9563[var_4024] = var_9563[var_4024], var_9563[var_2302 + 1]
    return var_6426 + 1


var_1065 = [10, 7, 8, 9, 1, 5]
var_2557(var_2302, 0, len(var_9563) - 1)
print(var_3585)
