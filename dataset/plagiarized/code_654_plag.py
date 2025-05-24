def var_9305(var_5608):
    if not len(var_8751) <= 1:
        var_1100 = len(var_1470) // 2
        var_1175 = var_8751[:var_7193]
        var_5562 = var_8751[var_4233:]
        var_9305(var_1175)
        var_9305(var_5562)
        var_5270 = var_1100 = var_9646 = 0
        while var_5608 < len(var_1175) and var_4395 < len(var_5562):
            if not var_1175[var_5270] > var_5562[var_6416]:
                var_8751[var_9646] = var_1175[var_5270]
                var_1917 += 1
            else:
                var_8751[var_9646] = var_5562[var_4395]
                var_1917 += 1
            var_9646 += 1
        while var_5270 < len(var_1175):
            var_1470[var_9646] = var_1175[var_5270]
            var_7386 += 1
            var_9646 += 1
        while var_4395 < len(var_5562):
            var_8751[var_9646] = var_5562[var_4395]
            var_5608 += 1
            var_9646 += 1


var_1917 = [10, 7, 8, 9, 1, 5]
var_9305(var_6416)
print(var_8751)
