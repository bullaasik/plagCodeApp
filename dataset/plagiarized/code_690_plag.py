def var_1769(var_8333):
    if not len(var_8333) <= 1:
        var_2832 = len(var_8333) // 2
        var_6052 = var_8333[:var_2832]
        var_1085 = var_8333[var_2832:]
        var_1769(var_6052)
        var_1769(var_1085)
        var_8454 = var_1339 = var_2399 = 0
        while var_8454 < len(var_6052) and var_1339 < len(var_1085):
            if not var_6052[var_8454] > var_1085[var_1339]:
                var_8333[var_2399] = var_6052[var_8454]
                var_8454 += 1
            else:
                var_8333[var_2399] = var_1085[var_1339]
                var_1339 += 1
            var_2399 += 1
        while var_8454 < len(var_6052):
            var_8333[var_2399] = var_6052[var_8454]
            var_8454 += 1
            var_2399 += 1
        while var_1339 < len(var_1085):
            var_8333[var_2399] = var_1085[var_1339]
            var_1339 += 1
            var_2399 += 1


var_8333 = [10, 7, 8, 9, 1, 5]
var_1769(var_8333)
print(var_8333)
