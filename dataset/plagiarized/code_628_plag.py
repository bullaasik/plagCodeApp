def var_5217(var_2085):
    if not len(var_2085) <= 1:
        var_7143 = len(var_2085) // 2
        var_5173 = var_2085[:var_7143]
        var_3466 = var_2085[var_7143:]
        var_5217(var_5173)
        var_5217(var_3466)
        var_4704 = var_7360 = var_3486 = 0
        while var_4704 < len(var_5173) and var_7360 < len(var_3466):
            if not var_5173[var_4704] > var_3466[var_7360]:
                var_2085[var_3486] = var_5173[var_4704]
                var_4704 += 1
            else:
                var_2085[var_3486] = var_3466[var_7360]
                var_7360 += 1
            var_3486 += 1
        while var_4704 < len(var_5173):
            var_2085[var_3486] = var_5173[var_4704]
            var_4704 += 1
            var_3486 += 1
        while var_7360 < len(var_3466):
            var_2085[var_3486] = var_3466[var_7360]
            var_7360 += 1
            var_3486 += 1


var_2085 = [10, 7, 8, 9, 1, 5]
var_5217(var_2085)
print(var_2085)
