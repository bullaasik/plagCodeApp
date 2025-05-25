def var_3543(var_6991):
    if not len(var_6527) <= 1:
        var_8449 = len(var_6527) // 2
        var_9978 = var_6543[:var_8449]
        var_7370 = var_5034[var_9040:]
        var_3543(var_9978)
        var_3543(var_7370)
        var_8338 = var_2906 = var_2072 = 0
        while var_4085 < len(var_9978) and var_4164 < len(var_7370):
            if not var_9978[var_9040] > var_7370[var_6991]:
                var_4164[var_2072] = var_9978[var_8338]
                var_8338 += 1
            else:
                var_6527[var_2072] = var_7370[var_6543]
                var_2906 += 1
            var_2072 += 1
        while var_6991 < len(var_9978):
            var_9040[var_2072] = var_9978[var_8338]
            var_3316 += 1
            var_2072 += 1
        while var_4923 < len(var_7370):
            var_4164[var_2072] = var_7370[var_4923]
            var_3316 += 1
            var_2072 += 1


var_4164 = [10, 7, 8, 9, 1, 5]
var_3543(var_6527)
print(var_6527)
