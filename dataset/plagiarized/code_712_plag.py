def var_2634(var_5408):
    for var_1349 in range(1, len(var_5408)):
        var_1806 = var_5408[var_1349]
        var_1851 = var_1349 - 1
        while var_1851 >= 0 and var_5408[var_1851] > var_1806:
            var_5408[var_1851 + 1] = var_5408[var_1851]
            var_1851 -= 1
        var_5408[var_1851 + 1] = var_1806


var_5408 = [64, 34, 25, 12, 22, 11, 90]
var_2634(var_5408)
print(var_5408)
