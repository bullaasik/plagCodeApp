def var_3619(var_4005):
    if not len(var_4005) <= 1:
        var_9768 = len(var_4005) // 2
        var_3721 = var_4005[:var_9768]
        var_8378 = var_4005[var_9768:]
        var_3619(var_3721)
        var_3619(var_8378)
        var_6070 = var_1914 = var_1765 = 0
        while var_6070 < len(var_3721) and var_1914 < len(var_8378):
            if not var_3721[var_6070] > var_8378[var_1914]:
                var_4005[var_1765] = var_3721[var_6070]
                var_6070 += 1
            else:
                var_4005[var_1765] = var_8378[var_1914]
                var_1914 += 1
            var_1765 += 1
        while var_6070 < len(var_3721):
            var_4005[var_1765] = var_3721[var_6070]
            var_6070 += 1
            var_1765 += 1
        while var_1914 < len(var_8378):
            var_4005[var_1765] = var_8378[var_1914]
            var_1914 += 1
            var_1765 += 1


var_4005 = [10, 7, 8, 9, 1, 5]
var_3619(var_4005)
print(var_4005)
