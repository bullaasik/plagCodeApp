def var_7719(var_1177):
    if   not len(var_1177) <= 1:
        var_2573 = len(var_1177) // 2
        var_2403 = var_1177[:var_2573]
        var_1606 = var_1177[var_2573:]
        var_7719(var_2403)
        var_7719(var_1606)
        var_3901 = var_5319 = var_2218 = 0
        while var_3901 < len(var_2403) and var_5319 < len(var_1606):
            if   not var_2403[var_3901] > var_1606[var_5319]:
                var_1177[var_2218] = var_2403[var_3901]
                var_3901 += 1
            else:
                var_1177[var_2218] = var_1606[var_5319]
                var_5319 += 1
            var_2218 += 1
        while var_3901 < len(var_2403):
            var_1177[var_2218] = var_2403[var_3901]
            var_3901 += 1
            var_2218 += 1
        while var_5319 < len(var_1606):
            var_1177[var_2218] = var_1606[var_5319]
            var_5319 += 1
            var_2218 += 1


var_1177 = [10, 7, 8, 9, 1, 5]
var_7719(var_1177)
print(var_1177)
