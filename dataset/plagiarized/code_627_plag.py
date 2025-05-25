def var_9555(var_2468):
    if not len(var_2468) <= 1:
        var_5842 = len(var_2468) // 2
        var_3378 = var_2468[:var_5842]
        var_9769 = var_2468[var_5842:]
        var_9555(var_3378)
        var_9555(var_9769)
        var_6999 = var_7293 = var_5066 = 0
        while var_6999 < len(var_3378) and var_7293 < len(var_9769):
            if not var_3378[var_6999] > var_9769[var_7293]:
                var_2468[var_5066] = var_3378[var_6999]
                var_6999 += 1
            else:
                var_2468[var_5066] = var_9769[var_7293]
                var_7293 += 1
            var_5066 += 1
        while var_6999 < len(var_3378):
            var_2468[var_5066] = var_3378[var_6999]
            var_6999 += 1
            var_5066 += 1
        while var_7293 < len(var_9769):
            var_2468[var_5066] = var_9769[var_7293]
            var_7293 += 1
            var_5066 += 1


var_2468 = [10, 7, 8, 9, 1, 5]
var_9555(var_2468)
print(var_2468)
