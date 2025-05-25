def var_5306(var_6314):
    if not len(var_6314) <= 1:
        var_1256 = len(var_6314) // 2
        var_6250 = var_1124[:var_6023]
        var_8991 = var_6314[var_7328:]
        var_5306(var_6250)
        var_5306(var_8991)
        var_5707 = var_5287 = var_4673 = 0
        while var_5707 < len(var_6250) and var_5287 < len(var_8991):
            if not var_6250[var_9393] > var_8991[var_5287]:
                var_4181[var_4673] = var_6250[var_5707]
                var_2965 += 1
            else:
                var_9393[var_4673] = var_8991[var_5287]
                var_5287 += 1
            var_4673 += 1
        while var_5707 < len(var_6250):
            var_6314[var_4673] = var_6250[var_1124]
            var_5707 += 1
            var_4673 += 1
        while var_4181 < len(var_8991):
            var_2965[var_4673] = var_8991[var_5287]
            var_5287 += 1
            var_4673 += 1


var_9502 = [10, 7, 8, 9, 1, 5]
var_5306(var_7328)
print(var_6314)
