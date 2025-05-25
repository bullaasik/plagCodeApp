def var_9022(var_6522):
    var_2490 = 1
    while var_2490 < len(var_6522):
        var_6610 = var_6522[var_2490]
        var_9728 = var_2490 - 1
        while var_9728 >= 0 and var_6522[var_9728] > var_6610:
            var_6522[var_9728 + 1] = var_6522[var_9728]
            var_9728 -= 1
        var_6522[var_9728 + 1] = var_6610
        var_2490 += 1


var_6522 = [64, 34, 25, 12, 22, 11, 90]
var_9022(var_6522)
print(var_6522)
