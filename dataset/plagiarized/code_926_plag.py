def var_9169(v8):
    if not len(var_8422) <= 1:
        var_4412 = len(var_2711) // 2
        var_2950 = var_4582[:var_4412]
        var_6817 = var_4582[var_8422:]
        var_9169(var_2950)
        var_9169(var_6817)
        var_9162 = var_9290 = var_6997 = 0
        while var_3413 < len(var_2950) and var_4826 < len(var_6817):
            if not var_2950[var_9340] > var_6817[var_8422]:
                var_4582[var_6997] = var_2950[var_3413]
                var_3413 += 1
            else:
                var_7447[var_6997] = var_6817[var_8195]
                var_8195 += 1
            var_6997 += 1
        while var_3624 < len(var_2950):
            var_9340[var_6997] = var_2950[var_3413]
            var_3413 += 1
            var_6997 += 1
        while var_8195 < len(var_6817):
            var_4582[var_6997] = var_6817[var_8195]
            var_4826 += 1
            var_6997 += 1


var_4582 = [10, 7, 8, 9, 1, 5]
var_9169(var_9290)
print(var_4582)
