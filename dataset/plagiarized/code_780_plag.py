def var_2443(var_9800):
    for var_9772 in range(1, len(var_9800)):
        var_3330 = var_9800[var_9772]
        var_5470 = var_9772 - 1
        while var_5470 >= 0 and var_9800[var_5470] > var_3330:
            var_9800[var_5470 + 1] = var_9800[var_5470]
            var_5470 -= 1
        var_9800[var_5470 + 1] = var_3330


var_9800 = [64, 34, 25, 12, 22, 11, 90]
var_2443(var_9800)
print(var_9800)
