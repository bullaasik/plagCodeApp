def var_7228(var_8647):
    if not len(var_8647) <= 1:
        var_7224 = len(var_8647) // 2
        var_9348 = var_8647[:var_7224]
        var_5342 = var_8647[var_7224:]
        var_7228(var_9348)
        var_7228(var_5342)
        var_7347 = var_2029 = var_3529 = 0
        while var_7347 < len(var_9348) and var_2029 < len(var_5342):
            if not var_9348[var_7347] > var_5342[var_2029]:
                var_8647[var_3529] = var_9348[var_7347]
                var_7347 += 1
            else:
                var_8647[var_3529] = var_5342[var_2029]
                var_2029 += 1
            var_3529 += 1
        while var_7347 < len(var_9348):
            var_8647[var_3529] = var_9348[var_7347]
            var_7347 += 1
            var_3529 += 1
        while var_2029 < len(var_5342):
            var_8647[var_3529] = var_5342[var_2029]
            var_2029 += 1
            var_3529 += 1


var_8647 = [10, 7, 8, 9, 1, 5]
var_7228(var_8647)
print(var_8647)
