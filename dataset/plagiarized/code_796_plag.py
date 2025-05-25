def var_1461(var_3977):
    var_8486 = 1
    while var_8486 < len(var_3977):
        var_3595 = var_3977[var_8486]
        var_9924 = var_8486 - 1
        while var_9924 >= 0 and var_3977[var_9924] > var_3595:
            var_3977[var_9924 + 1] = var_3977[var_9924]
            var_9924 -= 1
        var_3977[var_9924 + 1] = var_3595
        var_8486 += 1


var_3977 = [64, 34, 25, 12, 22, 11, 90]
var_1461(var_3977)
print(var_3977)
