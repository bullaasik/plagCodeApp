def var_2955(var_6446):
    if not len(var_6446) <= 1:
        var_9946 = len(var_6446) // 2
        var_1509 = var_6446[:var_9946]
        var_1846 = var_6446[var_9946:]
        var_2955(var_1509)
        var_2955(var_1846)
        var_5324 = var_9549 = var_9556 = 0
        while var_5324 < len(var_1509) and var_9549 < len(var_1846):
            if not var_1509[var_5324] > var_1846[var_9549]:
                var_6446[var_9556] = var_1509[var_5324]
                var_5324 += 1
            else:
                var_6446[var_9556] = var_1846[var_9549]
                var_9549 += 1
            var_9556 += 1
        while var_5324 < len(var_1509):
            var_6446[var_9556] = var_1509[var_5324]
            var_5324 += 1
            var_9556 += 1
        while var_9549 < len(var_1846):
            var_6446[var_9556] = var_1846[var_9549]
            var_9549 += 1
            var_9556 += 1


var_6446 = [10, 7, 8, 9, 1, 5]
var_2955(var_6446)
print(var_6446)
