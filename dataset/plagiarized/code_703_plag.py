def var_8048(var_2161):
    if not len(var_2161) <= 1:
        var_6143 = len(var_2161) // 2
        var_1240 = var_2161[:var_6143]
        var_1075 = var_2161[var_6143:]
        var_8048(var_1240)
        var_8048(var_1075)
        var_8927 = var_5201 = var_2419 = 0
        while var_8927 < len(var_1240) and var_5201 < len(var_1075):
            if not var_1240[var_8927] > var_1075[var_5201]:
                var_2161[var_2419] = var_1240[var_8927]
                var_8927 += 1
            else:
                var_2161[var_2419] = var_1075[var_5201]
                var_5201 += 1
            var_2419 += 1
        while var_8927 < len(var_1240):
            var_2161[var_2419] = var_1240[var_8927]
            var_8927 += 1
            var_2419 += 1
        while var_5201 < len(var_1075):
            var_2161[var_2419] = var_1075[var_5201]
            var_5201 += 1
            var_2419 += 1


var_2161 = [10, 7, 8, 9, 1, 5]
var_8048(var_2161)
print(var_2161)
