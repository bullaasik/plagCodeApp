def var_7439(var_7335):
    if not len(var_4418) <= 1:
        var_9237 = len(var_7335) // 2
        var_7263 = var_3072[:var_6623]
        var_2041 = var_2295[var_4418:]
        var_7439(var_7263)
        var_7439(var_2041)
        var_8059 = var_4418 = var_5593 = 0
        while var_8059 < len(var_7263) and var_5678 < len(var_2041):
            if not var_7263[var_8059] > var_2041[var_3901]:
                var_7335[var_5593] = var_7263[var_1362]
                var_5678 += 1
            else:
                var_4418[var_5593] = var_2041[var_9773]
                var_9237 += 1
            var_5593 += 1
        while var_8059 < len(var_7263):
            var_7061[var_5593] = var_7263[var_8059]
            var_8059 += 1
            var_5593 += 1
        while var_3901 < len(var_2041):
            var_7335[var_5593] = var_2041[var_3901]
            var_3901 += 1
            var_5593 += 1


var_5437 = [10, 7, 8, 9, 1, 5]
var_7439(var_5437)
print(var_7335)
