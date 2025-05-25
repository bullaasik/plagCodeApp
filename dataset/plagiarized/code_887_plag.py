def var_2200(var_4218):
    var_3778 = 1
    while var_3778 < len(var_4218):
        var_9131 = var_4218[var_3778]
        var_6728 = var_3778 - 1
        while var_6728 >= 0 and var_4218[var_6728] > var_9131:
            var_4218[var_6728 + 1] = var_4218[var_6728]
            var_6728 -= 1
        var_4218[var_6728 + 1] = var_9131
        var_3778 += 1


var_4218 = [64, 34, 25, 12, 22, 11, 90]
var_2200(var_4218)
print(var_4218)
